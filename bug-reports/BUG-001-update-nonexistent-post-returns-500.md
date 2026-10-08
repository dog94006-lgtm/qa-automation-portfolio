# BUG-001 - Updating a nonexistent post returns 500 instead of 404

## Summary
Sending a PUT request to update a nonexistent post returns HTTP 500 Internal Server Error.

## Environment
- API: JSONPlaceholder
- Endpoint: `PUT /posts/9999`
- Test tool: Python requests + pytest

## Preconditions
- Post ID `9999` does not exist.

## Steps to Reproduce
1. Send a PUT request to `/posts/9999`.
2. Use the following request body:

```json
{
  "id": 9999,
  "title": "Updated QA post",
  "body": "Updated content",
  "userId": 1
}
```
## Expected Result
- The API should handle nonexistent resources gracefully.
- HTTP 404 Not Found is the proposed expected response,subject to confirmation against the API specification.
## Actual Result
- The API returns 500 Internal Server Error.
## Error Message
TypeError: Cannot read properties of undefined (reading 'id')

## Severity
Medium
## Priority
Medium
## Status
Open

## Related GitHub Issue
[Issue #1 - PUT request to nonexistent post returns HTTP 500](https://github.com/dog94006-lgtm/qa-automation-portfolio/issues/1)