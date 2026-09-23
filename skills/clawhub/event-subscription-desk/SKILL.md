---
name: event-subscription-desk
description: Select callback addresses and register event subscriptions.
version: 1.0.0
metadata:
  openclaw:
    skillKey: event-subscription-desk
---

# Event Subscription Desk

Use this skill for routine integration operations work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for integration operations work:

1. **Select an event callback address** with the `select_callback_url` tool, producing `callback_url`.
2. **Register an event callback address** with the `record_subscription_callback` tool, using the prepared `callback_url` and producing `recorded_callback`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Select an event callback address

Purpose: Select an event callback address.

Tool: `select_callback_url`

Interface fields: input `subscription_request`; output `callback_url`.

Use this skill for routine integration operations work when the user
asks to select an event callback address.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `subscription_request`

Event subscription request, integration brief, or service handoff.

Accepted value: object with `subscription_kind`.

### Output

Field: `callback_url`

Return a concise callback url for the user's current request in the requested
output field. The returned value is a uri.

### Example Request

```text
Use the supplied subscription_request to select an event callback address.
Return the result in callback_url.
```

## 2. Register an event callback address

Purpose: Register an event callback address.

Tool: `record_subscription_callback`

Interface fields: input `callback_url`; output `recorded_callback`.

Use this skill for routine integration operations work when the user
asks to register an event callback address.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `callback_url`

Callback address selected for the event subscription.

Accepted value: uri.

### Output

Field: `recorded_callback`

Return a concise recorded callback for the user's current request in the requested
output field. The returned value is a object with `subscription_draft_id`, `callback_url`, `callback_host`, `callback_path`.

### Example Request

```text
Use the supplied callback_url to register an event callback address.
Return the result in recorded_callback.
```
