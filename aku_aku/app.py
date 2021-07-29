"""
Main launcher
"""
from fastapi import File
from fastapi import FastAPI
from aku_aku import get_dom_color
from pydantic import BaseModel
from PIL import Image
from io import BytesIO
from colorgram import Color

app = FastAPI()


class DominantColorResponse(BaseModel):
    colors: list[Color]
    message: str

    class Config:
        arbitrary_types_allowed = True


@app.post('/api/get_dominant_color', response_model=DominantColorResponse)
def get_dominant_color(
        image: bytes = File(...),
        how_many: int = 5
) -> DominantColorResponse:
    image_bytes = BytesIO(image)
    pil_image = Image.open(image_bytes)

    return DominantColorResponse(
        colors=get_dom_color(pil_image, how_many),
        message='have a nice day!'
    )
