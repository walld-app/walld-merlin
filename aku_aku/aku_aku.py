"""
Everything works here
"""
import uuid
from json import loads
from pathlib import Path
from urllib.parse import urljoin

from PIL import Image
import colorgram
from requests import get
from sqlalchemy.exc import OperationalError


def get_dom_color(img: Image, how_many: int) -> list[colorgram.Color]:
    """gets dominant color"""
    colors = colorgram.extract(img, how_many)
    return colors


def download(url, file_path):  # мне не нравится это все так как это можно заменить классом
    """
    Downloads file from first argument to second
    """
    request = get(url, stream=True)
    if request.status_code == 200:
        with open(file_path, 'wb') as file:
            for chunk in request.iter_content(1024):
                file.write(chunk)


def get_hex(colour):
    """
    gets colour object and returns string with hex
    """
    return '#%02x%02x%02x' % colour.rgb


def calc_and_insert(channel, method, _, body):
    """
    Main function that called by rmq
    calculates colours
    and inserts picture object into db
    """
    log.info(f'got \n {body}')
    channel.basic_ack(delivery_tag=method.delivery_tag)

    body = loads(body.decode())
    c_name = body['category']
    s_c_name = body['sub_category']
    tags = [db.get_row(Tag, name=i) for i in body['tags']]

    form = body['download_url'].split('.')[-1]

    filename = f'{str(uuid.uuid4())}.{form}'
    file_path = Path(PIC_FOLDER, c_name, s_c_name, filename)

    while file_path.exists():
        filename = str(uuid.uuid4())
        file_path = Path(PIC_FOLDER, c_name, s_c_name, filename)

    if not file_path.parent.exists():
        file_path.parent.mkdir(parents=True)

    download(body['download_url'], file_path)

    log.info('Downloaded!')

    colours = get_dom_color(file_path, how_many=5)

    body.pop('download_url')
    body.pop('preview_url')

    body['path'] = str(file_path)
    body['url'] = urljoin(PIC_URL, str(file_path.relative_to(PIC_FOLDER)))
    body['tags'] = tags
    body['category'] = db.get_row(Category, name=c_name).id  # getting ids
    body['sub_category'] = db.get_row(SubCategory, name=s_c_name).id
    body['colours'] = [get_hex(i) for i in colours]

    pic = Picture(**body)

    with db.get_session() as ses:
        try:
            ses.add(pic)
            log.info('successfully added pic!')
        except OperationalError as traceback:
            log.error(f'something happend! \n {traceback}')
