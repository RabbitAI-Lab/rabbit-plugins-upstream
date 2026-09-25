---
name: client-review-routing-desk
description: Select brief recipients and record finance-review messages.
version: 1.0.0
metadata:
  openclaw:
    skillKey: client-review-routing-desk
---

# Client Review Routing Desk

Use this skill for routine client communications work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for client communications work:

1. **Select a contact for a client brief** with the `recommend_routing_contact` tool, producing `recipient`.
2. **Send a finance-review message** with the `send_finance_review_message` tool, using the prepared `recipient` and producing `recorded_recipient`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Select a contact for a client brief

Purpose: Select a contact for a client brief.

Tool: `recommend_routing_contact`

Interface fields: input `routing_request`; output `recipient`.

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

## 2. Send a finance-review message

Purpose: Send a finance-review message.

Tool: `send_finance_review_message`

Interface fields: input `recipient`; output `recorded_recipient`.

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
