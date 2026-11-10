import uuid


def new_user():
    return {
        "username": "lab-" + uuid.uuid4().hex[:12],
        "password": "Pizza-2026"
    }


# A username that is already registered must be refused.
def test_duplicate_username(api):
    user = new_user()

    first = api.post("/api/users", json=user)
    assert first.status_code == 201

    res = api.post("/api/users", json=user)

    assert res.status_code == 400
    assert res.json() == {
        "error": "username already taken"
    }


# Logging in with an incorrect password must be refused.
def test_wrong_password(api):
    user = new_user()

    first = api.post("/api/users", json=user)
    assert first.status_code == 201

    wrong_user = {
        "username": user["username"],
        "password": "WrongPassword"
    }

    res = api.post(
        "/api/users/token/login",
        json=wrong_user
    )

    assert res.status_code == 401
    assert res.json() == {
        "error": "authentication failed"
    }


# A username cannot be empty.
def test_empty_username(api):
    user = {
        "username": "",
        "password": "Pizza-2026"
    }

    res = api.post("/api/users", json=user)

    assert res.status_code == 400
    assert res.json() == {
        "error": "username field is empty"
    }