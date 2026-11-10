# api-lab

| Characteristic | Blocks | Test Values |
|---|---|---|
| C1: Value of stars | Below 1, 1–5 (base), above 5 | 0, 3, 6 |
| C2: Type of stars | Whole number (base), decimal, text, missing | 3, 3.5, "3", no field |
| C3: Pizza | Exists (base), does not exist | New pizza, 999999999 |
| C4: Token | User's own (base), none, wrong length | auth, no header, token short |

## Test Coverage

| Characteristic | Block | Test Function |
|---|---|---|
| C1 | Below 1 | `test_stars_out_of_range[0]` |
| C1 | 1–5 (base) | `test_base_choice_is_saved` |
| C1 | Above 5 | `test_stars_out_of_range[6]` |
| C2 | Whole number (base) | `test_base_choice_is_saved` |
| C2 | Decimal | `test_decimal_stars` |
| C2 | Text | `test_text_stars` |
| C2 | Missing | `test_missing_stars` |
| C3 | Exists (base) | `test_base_choice_is_saved` |
| C3 | Does not exist | `test_nonexistent_pizza` |
| C4 | User's own token (base) | `test_base_choice_is_saved` |
| C4 | No token | `test_no_token` |
| C4 | Wrong token length | `test_short_token` |

## Step A2 Test Results

All 9 rating creation test cases passed.

- Base choice: PASSED
- Stars below 1: PASSED
- Stars above 5: PASSED
- Decimal stars: PASSED
- Text stars: PASSED
- Missing stars: PASSED
- Nonexistent pizza: PASSED
- No authentication token: PASSED
- Short authentication token: PASSED

**Result: 9 passed**
