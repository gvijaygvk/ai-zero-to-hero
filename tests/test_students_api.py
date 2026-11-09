import pytest
from fastapi.testclient import TestClient

from module2.fastapi import students_api

client = TestClient(students_api.app)


@pytest.fixture(autouse=True)
def reset():
    students_api.students.clear()


def test_create_student_201():
    r = client.post(
        "/students",
        json={"name": "Vijay", "age": 40, "skills": ["Python"], "email": "v@x.com"},
    )
    assert r.status_code == 201
    assert r.json() == {
        "name": "Vijay",
        "age": 40,
        "skills": ["Python"],
        "email": "v@x.com",
        "level": "beginner",
        "id": 1,
        "skill_count": 1,
    }


def test_skills_default_is_empty():
    r = client.post("/students", json={"name": "Asha", "age": 20, "email": "a@x.com"})
    assert r.json()["skills"] == []
    assert r.json()["skill_count"] == 0


def test_age_out_of_range_is_422():
    r = client.post("/students", json={"name": "Old", "age": 150, "email": "o@x.com"})
    assert r.status_code == 422
    assert r.json()["detail"][0]["loc"] == ["body", "age"]


def test_missing_name_is_422():
    assert client.post("/students", json={"age": 30}).status_code == 422


def test_list_students():
    client.post("/students", json={"name": "A", "age": 10, "email": "a@x.com"})
    client.post("/students", json={"name": "B", "age": 11, "email": "b@x.com"})
    assert [s["name"] for s in client.get("/students").json()] == ["A", "B"]


VALID = {"name": "Vijay", "age": 30, "email": "vijay@gmail.com"}


def test_missing_email_is_422():
    body = {"name": "Vijay", "age": 30}
    r = client.post("/students", json=body)
    assert r.status_code == 422
    err = r.json()["detail"][0]
    assert err["loc"] == ["body", "email"]
    assert err["type"] == "missing"


def test_invalid_email_is_422():
    r = client.post("/students", json={**VALID, "email": "Vijaygmail.com"})
    assert r.status_code == 422
    assert r.json()["detail"][0]["loc"] == ["body", "email"]


def test_invalid_level_is_422():
    r = client.post("/students", json={**VALID, "level": "interediate"})
    assert r.status_code == 422
    err = r.json()["detail"][0]
    assert err["loc"] == ["body", "level"]
    assert err["type"] == "literal_error"
