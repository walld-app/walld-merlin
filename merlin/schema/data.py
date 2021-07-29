from decimal import Decimal
from pydantic import BaseModel


class RGB(BaseModel):
    r: str
    g: str
    b: str

    class Config:
        orm_mode = True


class Color(BaseModel):
    rgb: RGB
    proportion: Decimal

    class Config:
        orm_mode = True


class DominantColorResponse(BaseModel):
    colors: list[Color]
    message: str
