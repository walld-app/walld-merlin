from httpx import AsyncClient
from merlin.app import app
from pytest import fixture, mark


@fixture()
async def client():
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client
