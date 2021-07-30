from httpx import AsyncClient
from merlin.schema.data import DominantColorResponse


__all__ = ["MerlinApiClient"]


class MerlinApiClient:
    def __init__(self, client: AsyncClient):
        self.client = client

    async def get_dominant_color(
        self, image: bytes, how_many: int = 5
    ) -> DominantColorResponse:
        response = await self.client.post(
            "/api/get_dominant_color",
            files=dict(image=image),
            data=dict(how_many=how_many),
        )
        return DominantColorResponse.construct(**response.json())
