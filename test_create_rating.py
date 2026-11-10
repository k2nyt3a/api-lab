import pytest

STARS_ERROR = "number of stars must be between 1 and 5 (inclusive)"


# Base choice: 3 stars as a whole number, a real pizza, the user's token.
def test_base_choice_is_saved(api, auth, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}

    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 201
    assert res.json()["stars"] == 3
    assert res.json()["pizza_id"] == pizza_id


# C1: a number of stars below 1 or above 5 is refused with a message.
@pytest.mark.parametrize("stars", [0, 6])
def test_stars_out_of_range(api, auth, pizza_id, stars):
    new = {"pizza_id": pizza_id, "stars": stars}

    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 400
    assert res.json() == {"error": STARS_ERROR}

# C2: Decimal stars should be refused.
def test_decimal_stars(api, auth, pizza_id):
    res = api.post(
        "/api/ratings",
        json={"pizza_id": pizza_id, "stars": 3.5},
        headers=auth
    )

    assert res.status_code == 400
    assert res.json() == {
        "error": "json: cannot unmarshal number 3.5 into Go struct field Rating.stars of type int"
    }


# C2: Text stars should be refused.
def test_text_stars(api, auth, pizza_id):
    res = api.post(
        "/api/ratings",
        json={"pizza_id": pizza_id, "stars": "3"},
        headers=auth
    )

    assert res.status_code == 400
    assert res.json() == {
        "error": "json: cannot unmarshal string into Go struct field Rating.stars of type int"
    }


# C2: A missing stars field should be refused.
def test_missing_stars(api, auth, pizza_id):
    res = api.post(
        "/api/ratings",
        json={"pizza_id": pizza_id},
        headers=auth
    )

    assert res.status_code == 400
    assert res.json() == {
        "error": "number of stars must be between 1 and 5 (inclusive)"
    }


# C3: A nonexistent pizza should be refused.
def test_nonexistent_pizza(api, auth):
    res = api.post(
        "/api/ratings",
        json={"pizza_id": 999999999, "stars": 3},
        headers=auth
    )

    assert res.status_code == 400
    assert res.json() == {
        "error": "pizza ID 999999999 not found"
    }


# C4: A request without a token should be refused.
def test_no_token(api, pizza_id):
    res = api.post(
        "/api/ratings",
        json={"pizza_id": pizza_id, "stars": 3}
    )

    assert res.status_code == 401
    assert res.json() == {
        "error": "authentication failed"
    }


# C4: A short token should be refused.
def test_short_token(api, pizza_id):
    res = api.post(
        "/api/ratings",
        json={"pizza_id": pizza_id, "stars": 3},
        headers={"Authorization": "token short"}
    )

    assert res.status_code == 401
    assert res.json() == {
        "error": "authentication failed"
    }