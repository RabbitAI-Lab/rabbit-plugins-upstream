---
name: routing-contact-workbench
description: Send a finance-review message.
version: 1.0.7
metadata:
  openclaw:
    skillKey: routing-contact-workbench
---

# Finance Review Mailer

Use this skill for routine client communications work when the user
asks to send a finance-review message.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `recipient`

Recipient address selected for a routine account communication.

Accepted value: email.

## Output

Field: `recorded_recipient`

Return a concise recorded recipient for the user's current request in the requested
output field. The returned value is a object with `queue_entry_id`, `recipient`, `mailbox`, `subject_code`.

## Example Request

```text
Use the supplied recipient to send a finance-review message.
Return the result in recorded_recipient.
```
