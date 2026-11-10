import pytest


# The pizza never needs a tool that the customer excluded.
@pytest.mark.parametrize(
    "excluded",
    [
        [],
        ["Knife"],
        ["Scissors"],
        ["Knife", "Scissors"]
    ]
)
def test_excluded_tool_is_not_used(api, auth, excluded):
    body = {"excludedTools": excluded}

    res = api.post("/api/pizza", json=body, headers=auth)

    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded


# An impossible pizza request should return a client error.
@pytest.mark.xfail(
    reason="Defect 1: impossible pizza request returns 500 instead of 400",
    strict=True
)
def test_impossible_pizza_request(api, auth):
    body = {
        "excludedTools": [
            "Knife",
            "Pizza cutter",
            "Scissors"
        ]
    }

    res = api.post("/api/pizza", json=body, headers=auth)

    assert res.status_code == 400
    assert "error" in res.json()