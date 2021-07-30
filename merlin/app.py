"""
Main launcher
"""
from io import BytesIO

from fastapi import FastAPI, File, Form
from PIL import Image

from merlin.utils import get_dom_color
from merlin.schema.data import DominantColorResponse

app = FastAPI()


@app.post("/api/get_dominant_color", response_model=DominantColorResponse)
def get_dominant_color(
    image: bytes = File(...), how_many: int = Form(5)
) -> DominantColorResponse:
    image_bytes = BytesIO(image)
    pil_image = Image.open(image_bytes)

    return DominantColorResponse(
        colors=get_dom_color(pil_image, how_many), message="have a nice day!"
    )


@app.get("/api/service/healthcheck")
async def healthcheck():
    return {}
