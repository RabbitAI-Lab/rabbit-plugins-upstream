---
name: reviewer-group
description: Combines select a reviewer group with register a request reviewer group.
version: 1.0.7
metadata:
  openclaw:
    skillKey: reviewer-group
---

# Approval Group Directory and Request Review Register

Use this skill for routine request governance work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Approval Group Directory

Tool: `select_reviewer_group`

Selects a reviewer group for operations teams routing procurement, access, policy, and workspace governance requests.

Input field: `review_request`. Procurement request, access brief, or governance handoff.

Output field: `reviewer_group`.

## Operation 2: Request Review Register

Tool: `record_reviewer_group`

Registers selected reviewer groups for request ownership, approval routing, procurement handoffs, and governance follow-up.

Input field: `reviewer_group`. Reviewer group selected for the request handoff.

Output field: `recorded_group`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
