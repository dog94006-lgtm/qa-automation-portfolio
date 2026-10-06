import pytest

def login(username, password):
    username = username.strip().lower()

    if username == "testuser" and password == "Test@1234":
        return True

    return False

@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("testuser", "Test@1234", True),
        ("testuser", "Wrong@1234", False),
        ("unknownuser", "Test@1234", False),
        ("unknownuser", "Wrong@1234", False),
        (" TestUser ", "Test@1234", True),
        ("testuser", "test@1234", False),
        ("testuser", " Test@1234 ", False),
    ],
)


def test_login(username,password,expected):
    result = login(username,password)

    assert result is expected


@pytest.fixture
def valid_user():
    return {
        "username": "testuser",
        "password": "Test@1234"
    }


def test_login_using_fixture(valid_user):
    result = login(
        valid_user["username"],
        valid_user["password"]
    )

    assert result is True