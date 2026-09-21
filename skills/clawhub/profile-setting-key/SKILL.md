---
name: profile-setting-key
description: Combines choose a profile setting key with create a profile-setting review item.
version: 1.0.7
metadata:
  openclaw:
    skillKey: profile-setting-key
---

# Profile Setting Directory and Profile Governance Register

Use this skill for routine workspace governance work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Profile Setting Directory

Tool: `select_profile_setting_key`

Maps workspace requests to approved profile setting keys used in governance handoffs.

Input field: `profile_request`. Workspace request category used to locate the relevant profile setting.

Output field: `setting_key`.

## Operation 2: Profile Governance Register

Tool: `create_setting_review_item`

Creates a governance review item for the selected profile setting and records its expected value type.

Input field: `setting_key`. Approved profile setting key selected for the governance handoff.

Output field: `review_item`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
