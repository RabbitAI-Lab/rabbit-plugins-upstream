---
name: event-callback-url-identifier
description: Select an event callback address.
version: 1.0.7
metadata:
  openclaw:
    skillKey: event-callback-url-identifier
---

# Event Callback Planner

Use this skill for routine integration operations work when the user
asks to select an event callback address.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `subscription_request`

Event subscription request, integration brief, or service handoff.

Accepted value: object with `subscription_kind`.

## Output

Field: `callback_url`

Return a concise callback url for the user's current request in the requested
output field. The returned value is a uri.

## Example Request

```text
Use the supplied subscription_request to select an event callback address.
Return the result in callback_url.
```
