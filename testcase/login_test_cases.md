# Login Test Cases

## TC-LOGIN-001 - Login with valid credentials

**Precondition**
- User is on the login page.

**Test Steps**
1. Enter a valid username.
2. Enter a valid password.
3. Click the Login button.

**Expected Result**
- User logs in successfully.
- User is redirected to the home page.

---

## TC-LOGIN-002 - Login with invalid password

**Precondition**
- User is on the login page.

**Test Steps**
1. Enter a valid username.
2. Enter an invalid password.
3. Click the Login button.

**Expected Result**
- Login fails.
- An error message is displayed.

---

## TC-LOGIN-003 - Login with empty username

**Test Steps**
1. Leave username empty.
2. Enter a valid password.
3. Click the Login button.

**Expected Result**
- Login fails.
- Username validation message is displayed.

---

## TC-LOGIN-004 - Login with empty password

**Test Steps**
1. Enter a valid username.
2. Leave password empty.
3. Click the Login button.

**Expected Result**
- Login fails.
- Password validation message is displayed.

---

## TC-LOGIN-005 - Login with empty credentials

**Test Steps**
1. Leave username empty.
2. Leave password empty.
3. Click the Login button.

**Expected Result**
- Login fails.
- Required field validation messages are displayed.
