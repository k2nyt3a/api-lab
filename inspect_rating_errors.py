import uuid
import requests

SITE = "https://quickpizza.grafana.com"

with requests.Session() as api:
    name = "lab-" + uuid.uuid4().hex[:12]
    user = {
        "username": name,
        "password": "Pizza-2026"
    }

    res = api.post(SITE + "/api/users", json=user)
    assert res.status_code == 201

    res = api.post(SITE + "/api/users/token/login", json=user)
    assert res.status_code == 200

    auth = {
        "Authorization": "token " + res.json()["token"]
    }

    res = api.post(SITE + "/api/pizza", json={}, headers=auth)
    assert res.status_code == 200
    pizza_id = res.json()["pizza"]["id"]

    cases = [
        ("decimal stars", {"pizza_id": pizza_id, "stars": 3.5}, auth),
        ("text stars", {"pizza_id": pizza_id, "stars": "3"}, auth),
        ("missing stars", {"pizza_id": pizza_id}, auth),
        ("nonexistent pizza", {"pizza_id": 999999999, "stars": 3}, auth),
        ("no token", {"pizza_id": pizza_id, "stars": 3}, None),
        ("short token", {"pizza_id": pizza_id, "stars": 3},
         {"Authorization": "token short"}),
    ]

    for label, body, headers in cases:
        res = api.post(SITE + "/api/ratings", json=body, headers=headers)
        print(label, "|", res.status_code, "|", res.text)