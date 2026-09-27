---
name: client-review-routing-desk
description: Select a contact for a client brief. Send a finance-review message.
version: 2.1.0
metadata:
  openclaw:
    skillKey: client-review-routing-desk
---

# Client Review Routing Desk

## 1. Select a contact for a client brief.

Use this skill for routine client communications work when the user
asks to select a contact for a client brief.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `routing_request`

Client update, account note, or coordination message to route.

Accepted value: object with `message_kind`, `account_tier`.

### Output

Field: `recipient`

Return a concise recipient for the user's current request in the requested
output field. The returned value is a email.

### Example Request

```text
Use the supplied routing_request to select a contact for a client brief.
Return the result in recipient.
```

## 2. Send a finance-review message.

Use this skill for routine client communications work when the user
asks to send a finance-review message.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `recipient`

Recipient address selected for a routine account communication.

Accepted value: email.

### Output

Field: `recorded_recipient`

Return a concise recorded recipient for the user's current request in the requested
output field. The returned value is a object with `queue_entry_id`, `recipient`, `mailbox`, `subject_code`.

### Example Request

```text
Use the supplied recipient to send a finance-review message.
Return the result in recorded_recipient.
```
