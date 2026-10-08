import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["userId"] == 1

def test_get_nonexistent_post():
    response = requests.get(f"{BASE_URL}/posts/9999")

    assert response.status_code == 404
    assert response.json() == {}

def test_create_post():
    payload = {
        "title": "QA test post",
        "body": "This is a test post.",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload
    )

    assert response.status_code == 201
    

    data = response.json()

    assert data["title"] == "QA test post"
    assert data["body"] == "This is a test post."
    assert data["userId"] == 1
    assert "id" in data
    assert isinstance(data["id"],int)
    print(response.json()["id"])


def test_update_post():
    payload = {
        "id": 1,
        "title": "Updated QA post",
        "body": "Updated content",
        "userId": 1
    }

    response = requests.put(
        f"{BASE_URL}/posts/1",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Updated QA post"
    assert data["body"] == "Updated content"
    assert data["userId"] == 1


def test_delete_post():
    response = requests.delete(
        f"{BASE_URL}/posts/1"
    )

    assert response.status_code == 200


def test_update_nonexistent_post():
    payload = {
        "id": 9999,
        "title": "Updated QA post",
        "body": "Updated content",
        "userId": 1
    }

    response = requests.put(
        f"{BASE_URL}/posts/9999",
        json=payload
    )

    print(response.status_code)
    print(response.text)