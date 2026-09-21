---
name: event-callback-url
description: Combines select an event callback address with register an event callback address.
version: 1.0.7
metadata:
  openclaw:
    skillKey: event-callback-url
---

# Event Callback Planner and Subscription Receipt Desk

Use this skill for routine integration operations work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Event Callback Planner

Tool: `select_callback_url`

Plans a callback address for integration teams coordinating event subscriptions, service handoffs, and account-update delivery.

Input field: `subscription_request`. Event subscription request, integration brief, or service handoff.

Output field: `callback_url`.

## Operation 2: Subscription Receipt Desk

Tool: `record_subscription_callback`

Registers callback destinations for event subscriptions used in integration, service coordination, and account-update handoffs.

Input field: `callback_url`. Callback address selected for the event subscription.

Output field: `recorded_callback`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
