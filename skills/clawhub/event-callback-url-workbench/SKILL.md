---
name: event-callback-url-workbench
description: Register an event callback address.
version: 1.0.7
metadata:
  openclaw:
    skillKey: event-callback-url-workbench
---

# Subscription Receipt Desk

Use this skill for routine integration operations work when the user
asks to register an event callback address.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `callback_url`

Callback address selected for the event subscription.

Accepted value: uri.

## Output

Field: `recorded_callback`

Return a concise recorded callback for the user's current request in the requested
output field. The returned value is a object with `subscription_draft_id`, `callback_url`, `callback_host`, `callback_path`.

## Example Request

```text
Use the supplied callback_url to register an event callback address.
Return the result in recorded_callback.
```
