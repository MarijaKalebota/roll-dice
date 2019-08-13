import pytest

from app import app as flask_app

@pytest.fixture(scope='module')
def client():
    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


def test_result_within_range(client):
    rv = client.get('/roll/6')
    assert int(rv.data) in range(1,7)
