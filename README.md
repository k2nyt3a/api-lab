# api-lab

## Input Domain Model — POST /api/ratings

| Characteristic | Blocks | Test Values |
|---|---|---|
| C1: Value of stars | Below 1, 1–5 (base), above 5 | 0, 3, 6 |
| C2: Type of stars | Whole number (base), decimal, text, missing | 3, 3.5, "3", no field |
| C3: Pizza | Exists (base), does not exist | New pizza, 999999999 |
| C4: Token | User's own (base), none, wrong length | auth, no header, token short |