import pytest


# Boundary values: only 1 to 5 stars are accepted.
# Rejected updates must leave the original rating unchanged.
@pytest.mark.parametrize(
    "stars, expected_status",
    [
        (0, 400),
        (1, 200),
        (5, 200),
        (6, 400),
    ]
)
def test_update_rating_boundary(api, auth, rating, stars, expected_status):
    path = f"/api/ratings/{rating['id']}"

    # Update the rating.
    res = api.put(
        path,
        json={"stars": stars},
        headers=auth
    )

    assert res.status_code == expected_status

    # Read the rating again to check the stored value.
    saved = api.get(path, headers=auth)

    assert saved.status_code == 200

    if expected_status == 200:
        assert saved.json()["stars"] == stars
    else:
        assert saved.json()["stars"] == 3