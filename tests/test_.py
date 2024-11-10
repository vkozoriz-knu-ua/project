from pytest import fixture

from src import app


@fixture
def client():
    with app.test_client() as client:
        yield client


def test(client):
    assert client.get("/api").status_code == 200
