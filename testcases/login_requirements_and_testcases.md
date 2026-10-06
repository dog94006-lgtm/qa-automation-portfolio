# Login Requirements and Test Cases

## 1. Feature Overview

The system provides a login function that allows registered users to access the application using their username and password.

---

## 2. Functional Requirements

### FR-LOGIN-001 - Required Fields
- Username is required.
- Password is required.
- If either field is empty, the user must not be able to log in.

### FR-LOGIN-002 - Valid Login
- A registered user must be able to log in using the correct username and password.
- After successful login, the user must be redirected to the home page.

### FR-LOGIN-003 - Invalid Credentials
- If the username or password is incorrect, login must fail.
- The user must remain on the login page.
- The system must display the following message:

`Invalid username or password.`

### FR-LOGIN-004 - Username Whitespace Handling
- Leading and trailing whitespace in the username must be removed before validation.
- Example:

`" testuser "` should be treated as `"testuser"`.

### FR-LOGIN-005 - Password Whitespace Handling
- Password input must not be automatically trimmed.
- Spaces entered in the password are treated as part of the password.

### FR-LOGIN-006 - Password Case Sensitivity
- Passwords are case-sensitive.
- Example:

If the correct password is:

`Test1234`

then:

`test1234`

must be treated as an incorrect password.

### FR-LOGIN-007 - Special Characters in Password
- Passwords may contain special characters.
- The following characters are supported:

`! @ # $ % ^ & *`

### FR-LOGIN-008 - Username Case Sensitivity
- Usernames are not case-sensitive.
- Example:

`TestUser`

and

`testuser`

must be treated as the same username.

---

## 3. Validation Requirements

### VR-LOGIN-001 - Empty Username
If the username field is empty and the Login button is clicked, the following validation message must be displayed:

`Username is required.`

### VR-LOGIN-002 - Empty Password
If the password field is empty and the Login button is clicked, the following validation message must be displayed:

`Password is required.`

### VR-LOGIN-003 - Both Fields Empty
If both username and password are empty:
- Login must fail.
- Both validation messages must be displayed.

Expected messages:

`Username is required.`

`Password is required.`

---

## 4. Test Data

Use the following registered test account:

| Field | Value |
|---|---|
| Username | testuser | testuser1 |
| Password | Test@1234 | Test!1234 |

The following values may be used as invalid test data:

| Type | Value |
|---|---|
| Invalid Username | unknownuser |
| Invalid Password | Wrong@1234 |
| Wrong Password Case | test@1234 |

---

## 5. Test Case Writing Rules

Each test case should contain:

- Test Case ID
- Test Case Title
- Related Requirement
- Precondition
- Test Steps
- Test Data
- Expected Result

Example structure:

## TC-LOGIN-001 - Login with valid credentials

**Related Requirement**
- FR-LOGIN-002

**Precondition**
- User is on the login page.
- The test account exists.

**Test Data**
- Username: testuser
- Password: Test@1234

**Test Steps**
1. Enter the username.
2. Enter the password.
3. Click the Login button.

**Expected Result**
- Login succeeds.
- User is redirected to the home page.

---

# Your Test Cases

Write your test cases below this line.

## TC-LOGIN-002 - Login with empty password

**Related Requirement**
- FR-LOGIN-001
- VR-LOGIN-002

**Precondition**
- User is on the login page.
- The test account exists.

**Test Data**
- Username: testuser
- Password: 

**Test Steps**
1. Enter the username.
2. Click the Login button.

**Expected Result**
- Login fail.
- User is remain on the login page.
- `Password is required.` message is displayed.

## TC-LOGIN-003 - Login with empty username

**Related Requirement**
- FR-LOGIN-001
- VR-LOGIN-001

**Precondition**
- User is on the login page.
- The test account exists.

**Test Data**
- Username: 
- Password: Test@1234

**Test Steps**
1. Enter the password.
2. Click the Login button.

**Expected Result**
- Login fail.
- User is remain on the login page.
- `Username is required.` message is displayed.

## TC-LOGIN-004 - Login with empty credentials

**Related Requirement**
- FR-LOGIN-001
- VR-LOGIN-003

**Precondition**
- User is on the login page.
- The test account exists.

**Test Data**
- Username: 
- Password: 

**Test Steps**
1. Click the Login button.

**Expected Result**
- Login fail.
- User is remain on the login page.
- `Username is required.``Password is required.` messages are both displayed.

## TC-LOGIN-005 - Login with invalid password

**Related Requirement**
- FR-LOGIN-003

**Precondition**
- User is on the login page.
- The test account exists.

**Test Data**
- Username: testuser
- Password: Wrong@1234

**Test Steps**
1. Enter the username.
2. Enter the password.
3. Click the Login button.

**Expected Result**
- Login fail.
- User is remain on the login page.
- `Invalid username or password.` message is displayed.

## TC-LOGIN-006 - Login with invalid username

**Related Requirement**
- FR-LOGIN-003

**Precondition**
- User is on the login page.
- The test account not exists.

**Test Data**
- Username: unknownuser
- Password: Test@1234

**Test Steps**
1. Enter the username.
2. Enter the password.
3. Click the Login button.

**Expected Result**
- Login fail.
- User is remain on the login page.
- `Invalid username or password.` message is displayed.

## TC-LOGIN-007 - Login with invalid credentials

**Related Requirement**
- FR-LOGIN-003

**Precondition**
- User is on the login page.
- The test account not exists.

**Test Data**
- Username: unknownuser
- Password: Wrong@1234

**Test Steps**
1. Enter the username.
2. Enter the password.
3. Click the Login button.

**Expected Result**
- Login fail.
- User is remain on the login page.
- `Invalid username or password.` message is displayed.

## TC-LOGIN-008 - Login with Leading and trailing whitespace in the username

**Related Requirement**
- FR-LOGIN-004

**Precondition**
- User is on the login page.
- The test account exists.

**Test Data**
- Username:  testuser 
- Password: Test@1234

**Test Steps**
1. Enter the username.
2. Enter the password.
3. Click the Login button.

**Expected Result**
- Login succeeds.
- User is redirected to the home page.

## TC-LOGIN-009 - Login with Leading and trailing whitespace in the password

**Related Requirement**
- FR-LOGIN-005

**Precondition**
- User is on the login page.
- The test account exists.

**Test Data**
- Username: testuser
- Password:  Test@1234 

**Test Steps**
1. Enter the username.
2. Enter the password.
3. Click the Login button.

**Expected Result**
- Login fail.
- User is remain on the login page.
- `Invalid username or password.` message is displayed.

## TC-LOGIN-010 - Login with Leading and trailing whitespace in credentials

**Related Requirement**
- FR-LOGIN-004
- FR-LOGIN-005

**Precondition**
- User is on the login page.
- The test account exists.

**Test Data**
- Username:  testuser 
- Password:  Test@1234 

**Test Steps**
1. Enter the username.
2. Enter the password.
3. Click the Login button.

**Expected Result**
- Login fail.
- User is remain on the login page.
- `Invalid username or password.` message is displayed.

## TC-LOGIN-011 - Login with Password Case Sensitivity

**Related Requirement**
- FR-LOGIN-006

**Precondition**
- User is on the login page.
- The test account exists.

**Test Data**
- Username:  testuser 
- Password:  TesT@1234 

**Test Steps**
1. Enter the username.
2. Enter the password.
3. Click the Login button.

**Expected Result**
- Login fail.
- User is remain on the login page.
- `Invalid username or password.` message is displayed.

## TC-LOGIN-012 - Login with Username Case insensitivity

**Related Requirement**
- FR-LOGIN-008

**Precondition**
- User is on the login page.
- The test account exists.

**Test Data**
- Username: Testuser
- Password: Test@1234

**Test Steps**
1. Enter the username.
2. Enter the password.
3. Click the Login button.

**Expected Result**
- Login succeeds.
- User is redirected to the home page.


## TC-LOGIN-013 - Login with credentials Case Sensitivity

**Related Requirement**
- FR-LOGIN-006
- FR-LOGIN-008

**Precondition**
- User is on the login page.
- The test account exists.

**Test Data**
- Username: Testuser
- Password: TesT@1234

**Test Steps**
1. Enter the username.
2. Enter the password.
3. Click the Login button.

**Expected Result**
- Login fail.
- User is remain on the login page.
- `Invalid username or password.` message is displayed.

## TC-LOGIN-014 - Login with Permitted Special Characters in Password

**Related Requirement**
- FR-LOGIN-003
- FR-LOGIN-007

**Precondition**
- User is on the login page.
- The test account exists.

**Test Data**
- Username: testuser1
- Password: Test!1234

**Test Steps**
1. Enter the username.
2. Enter the password.
3. Click the Login button.

**Expected Result**
- Login succeeds.
- User is redirected to the home page.

## TC-LOGIN-015 - Login with Unpermitted Special Characters in Password

**Related Requirement**
- FR-LOGIN-003
- FR-LOGIN-007

**Precondition**
- User is on the login page.
- The test account exists.

**Test Data**
- Username: testuser
- Password: Test-1234

**Test Steps**
1. Enter the username.
2. Enter the password.
3. Click the Login button.

**Expected Result**
- Login fail.
- User is remain on the login page.
- `Invalid username or password.` message is displayed.