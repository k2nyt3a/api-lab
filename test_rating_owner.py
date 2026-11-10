# Another user must not read someone else's rating.
def test_other_user_cannot_read(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    res = api.get(path, headers=other_auth)

    print("Read status:", res.status_code)

    assert 400 <= res.status_code <= 499

    # The owner should still be able to read the rating.
    owner_res = api.get(path, headers=auth)

    assert owner_res.status_code == 200
    assert owner_res.json() == rating


# Another user must not update someone else's rating.
def test_other_user_cannot_update(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    res = api.put(
        path,
        json={"stars": 5},
        headers=other_auth
    )

    print("Update status:", res.status_code)

    assert 400 <= res.status_code <= 499

    # The rating must still have its original 3 stars.
    owner_res = api.get(path, headers=auth)

    assert owner_res.status_code == 200
    assert owner_res.json() == rating


# Another user must not delete someone else's rating.
def test_other_user_cannot_delete(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"

    res = api.delete(path, headers=other_auth)

    print("Delete status:", res.status_code)

    assert 400 <= res.status_code <= 499

    # The owner's rating must still exist and remain unchanged.
    owner_res = api.get(path, headers=auth)

    assert owner_res.status_code == 200
    assert owner_res.json() == rating