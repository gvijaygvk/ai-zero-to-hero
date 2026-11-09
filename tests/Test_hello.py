from fastapi.testclient import TestClient

from module2.fastapi.hello_api import app

client = TestClient(app)


def test_home():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello, FastAPI"}


def test_greet_path_param():
    assert client.get("/greet/Vijay").json() == {"greeting": "Hello, Vijay"}


def test_add_query_params():
    assert client.get("/add?a=2&b=3").json()["sum"] == 5


def test_add_default_b():
    assert client.get("/add?a=7").json()["sum"] == 7


def test_add_bad_type_is_422():
    assert client.get("/add?a=two").status_code == 422


def test_add_missing_a_is_422():
    assert client.get("/add").status_code == 422


def test_square():
    assert client.get("/square/2").json()["square"] == 4


def test_square_with_param():
    assert client.get("/square/3?negate=true").json()["square"] == -9


def test_square_bad_422():
    assert client.get("/square/abc").status_code == 422
