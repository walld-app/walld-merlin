from httpx import AsyncClient
from merlin.app import app
from pytest import fixture, mark


@fixture()
def client():
    yield AsyncClient(app=app, base_url="http://testserver")
