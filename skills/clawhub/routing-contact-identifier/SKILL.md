---
name: routing-contact-identifier
description: Select a contact for a client brief.
version: 1.0.7
metadata:
  openclaw:
    skillKey: routing-contact-identifier
---

# Client Brief Routing Desk

Use this skill for routine client communications work when the user
asks to select a contact for a client brief.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `routing_request`

Client update, account note, or coordination message to route.

Accepted value: object with `message_kind`, `account_tier`.

## Output

Field: `recipient`

Return a concise recipient for the user's current request in the requested
output field. The returned value is a email.

## Example Request

```text
Use the supplied routing_request to select a contact for a client brief.
Return the result in recipient.
```
