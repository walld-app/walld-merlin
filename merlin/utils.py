from PIL import Image
import colorgram

from merlin.schema.data import Color


def get_dom_color(img: Image, how_many: int) -> list[Color]:
    """gets dominant color"""
    colors = colorgram.extract(img, how_many)
    result = [Color.from_orm(color) for color in colors]
    return result


def get_hex(colour):
    """
    gets colour object and returns string with hex
    """
    return '#%02x%02x%02x' % colour.rgb
