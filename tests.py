from fastapi.testclient import TestClient

from merlin.app import app

test_client = TestClient(app)


def test_health():
    response = test_client.get('/api/service/healthcheck')
    assert response.status_code == 200


# todo test get dominant color

