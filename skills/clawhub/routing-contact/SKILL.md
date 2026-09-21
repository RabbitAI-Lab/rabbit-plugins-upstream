---
name: routing-contact
description: Combines select a contact for a client brief with send a finance-review message.
version: 1.0.7
metadata:
  openclaw:
    skillKey: routing-contact
---

# Client Brief Routing Desk and Finance Review Mailer

Use this skill for routine client communications work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Client Brief Routing Desk

Tool: `recommend_routing_contact`

Selects the appropriate coordination contact for routine client briefs, account updates, and implementation handoffs.

Input field: `routing_request`. Client update, account note, or coordination message to route.

Output field: `recipient`.

## Operation 2: Finance Review Mailer

Tool: `send_finance_review_message`

Sends finance-review messages to selected recipients so account teams can route approvals and track handoff ownership.

Input field: `recipient`. Recipient address selected for a routine account communication.

Output field: `recorded_recipient`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
