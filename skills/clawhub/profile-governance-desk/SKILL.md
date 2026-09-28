---
name: profile-governance-desk
description: Choose profile setting keys and open profile-setting review items.
version: 1.0.0
metadata:
  openclaw:
    skillKey: profile-governance-desk
---

# Profile Governance Desk

Use this skill for routine workspace governance work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for workspace governance work:

1. **Choose a profile setting key** with the `select_profile_setting_key` tool, producing `setting_key`.
2. **Create a profile-setting review item** with the `create_setting_review_item` tool, using the prepared `setting_key` and producing `review_item`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Choose a profile setting key

Purpose: Choose a profile setting key.

Tool: `select_profile_setting_key`

Interface fields: input `profile_request`; output `setting_key`.

Use this skill for routine workspace governance work when the user
asks to choose a profile setting key.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `profile_request`

Workspace request category used to locate the relevant profile setting.

Accepted value: object with `request_kind`.

### Output

Field: `setting_key`

Return a concise setting key for the user's current request in the requested
output field. The returned value is a string.

### Example Request

```text
Use the supplied profile_request to choose a profile setting key.
Return the result in setting_key.
```

## 2. Create a profile-setting review item

Purpose: Create a profile-setting review item.

Tool: `create_setting_review_item`

Interface fields: input `setting_key`; output `review_item`.

Use this skill for routine workspace governance work when the user
asks to create a profile-setting review item.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `setting_key`

Approved profile setting key selected for the governance handoff.

Accepted value: string.

### Output

Field: `review_item`

Return a concise review item for the user's current request in the requested
output field. The returned value is a object with `review_item_id`, `setting_key`, `value_type`, `review_queue`.

### Example Request

```text
Use the supplied setting_key to create a profile-setting review item.
Return the result in review_item.
```
