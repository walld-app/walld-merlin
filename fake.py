import json
from pathlib import Path

import colorgram
import requests
from walld_db.helpers import DB, Rmq
from walld_db.models import Picture

from config import (DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER, RMQ_HOST,
                    RMQ_PASS, RMQ_PORT, RMQ_USER, PIC_FOLDER)


def get_dom_color(img: str, how_many: int):
    '''gets dominant color'''
    colors = colorgram.extract(img, how_many)
    return colors

def download(url, file_path): # мне не нравится это все так как это можно заменить классом
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)

def get_hex(colour): # кандидат на удаление
    return '#%02x%02x%02x' % colour.rgb

# TODO МОГУ И КЛАСС ЗАМУТИТЬ С ПИКЧЕЙ И ФУНКЦЙИЕЙ ГО СКЛ

def calc_and_insert(ch, method, properties, body):
    print('got some')
    ch.basic_ack(delivery_tag=method.delivery_tag)
    body = json.loads(body.decode())
    c_name = body['category']
    s_c_name = body['sub_category']

    file_path = Path(PIC_FOLDER, c_name, s_c_name, 'll.png') # TODO Имя дай номральное
    if not file_path.exists():
        file_path.mkdir(parents=True)
    download(body['download_url'], file_path)
    body['path'] = file_path
    body.pop('download_url')
    body.pop('preview_url')
    body['category'] = db.get_category(category_name=c_name).category_id
    tags = [db.get_tag(tag_name=i) for i in body['tags']]
    body['tags'] = tags
    body['sub_category'] = db.get_sub_category(sub_category_name=s_c_name).sub_category_id
    colours = get_dom_color(file_path, how_many=5)
    body['colours'] = [get_hex(i).encode() for i in colours]

    pic = Picture(**body)
    print(pic.__dict__)
    with db.get_session() as ses:
        ses.add(pic)

db = DB(host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        passwd=DB_PASS,
        name=DB_NAME)

def do_stuff():

    rmq = Rmq(host=RMQ_HOST,
              port=RMQ_PORT,
              user=RMQ_USER,
              passw=RMQ_PASS)

    rmq.channel.basic_qos(prefetch_count=1)
    rmq.channel.basic_consume(queue='go_sql',
                              on_message_callback=calc_and_insert)

    rmq.channel.start_consuming()

if __name__ == '__main__':

    do_stuff()
