from merlin.schema.client import MerlinApiClient
from pytest import mark

pytestmark = mark.asyncio


class TestAllViews:
    TEST_IMAGE = "tests/test_image.jpg"

    async def test_health(self, client):
        response = await client.get("/api/service/healthcheck")
        assert response.status_code == 200

    async def test_dominant_color(self, client):
        with open(self.TEST_IMAGE, "rb") as file:
            response = await client.post(
                "/api/get_dominant_color",
                files=dict(
                    image=file,
                ),
                data=dict(how_many=2),
            )

        assert response.status_code == 200
        assert response.json() == {
            "colors": [
                {
                    "proportion": 0.659147129702038,
                    "rgb": {"b": "30", "g": "25", "r": "23"},
                },
                {
                    "proportion": 0.34085287029796196,
                    "rgb": {"b": "27", "g": "31", "r": "37"},
                },
            ],
            "message": "have a nice day!",
        }

    async def test_merlin_client(self, client):
        client = MerlinApiClient(client)
        with open(self.TEST_IMAGE, "rb") as file:
            response = await client.get_dominant_color(file.read(), how_many=2)

        assert response.message == "have a nice day!"
        assert len(response.colors) == 2
