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
