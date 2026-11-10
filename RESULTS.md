# API Lab Results

## Part 0
- Step 0.1, number of pizza names: 18
- Step 0.2
    - status code: 200
    - content type: application/json
    - WSALB cookie: Present
- Step 0.3, status code without a token: 401 Unauthorized
- Step 0.4, name of your pizza: The Poor Calzone
- Step 0.5: Successfully tested GET and POST requests using Python requests. Both returned status 200.
- Step 0.6: Created the first pytest test. Verified that it fails with an incorrect pizza name and passes with the correct name.
- Step 0.7: test_vegetarian_pizza PASSED
- Step 0.8: test_pizza_without_token_is_refused and test_tools_are_listed PASSED  
- Step 0.9: Created a unique test user, logged in successfully,
  and confirmed that the new user had no ratings.
  Session cookies were retained.
- Step 0.10: All 4 test pass
- Step 0.11: test_new_user_has_no_ratings PASSED  
- Step 0.12: results of the three runs without a session
  - Run 1: PASS 
  - Run 2: FAIL
  - Run 3: PASS 
- Step 0.13: test_new_user_has_no_ratings PASSED 
- Step 0.14: test_read_rating, test_update_rating, and test_delete_rating PASSED   
- Step 0.15: test_duplicate_username, test_wrong_password, and test_empty_username PASSED         
- Step 0.16, blocks of "how many of the three tools are excluded":
  - B1: 0 tools excluded
  - B2: 1 tool excluded
  - B3: 2 tools excluded
  - B4: 3 tools excluded

## Defect Report

- Title: API returns HTTP 500 for an impossible pizza request
- Request: POST /api/pizza with all three tools excluded
- Expected result: HTTP 400 with a JSON error message
- Actual result: HTTP 500 with an empty body
- Severity: Medium

## Part A

- Step A4, status codes when another user accesses the owner's rating:
  - Read (GET): 404
  - Update (PUT): 400
  - Delete (DELETE): 400

## Part B

1. API tests can find server connection issues and wrong HTTP responses that unit tests with stubs might miss. Unit tests are still useful because they're faster and easier to debug.

2. Each test uses a new user to avoid affecting other people's data. For Project 2, we'll also create our own test data instead of using other groups' data.

3. We use one session to keep the cookies and stay connected to the same server. Without it, login might fail because requests could go to different servers.

4. Excluding all three tools caused the bug. A 500 error doesn't explain what went wrong, while a 400 gives a useful message. We keep the test as xfail so we know when the bug gets fixed.

5. Base choice needs 9 tests: 1 + 2 + 3 + 1 + 2 = 9. All combinations need 72 tests: 3 × 4 × 2 × 3 = 72.

6. The other user got [READ], [UPDATE], and [DELETE] for reading, updating, and deleting the rating. I expected a 4xx error for all three. Any different 4xx code isn't necessarily a bug because access was still denied.

7. The API returned a list of ratings even with a fake token. This is a security bug because someone could access ratings without a valid account.

8. API tests are better for checking status codes and response data. UI tests can check how the website looks and whether buttons work.