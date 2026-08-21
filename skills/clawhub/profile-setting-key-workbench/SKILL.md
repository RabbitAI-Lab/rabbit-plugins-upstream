---
name: profile-setting-key-workbench
description: Create a profile-setting review item.
version: 1.0.7
metadata:
  openclaw:
    skillKey: profile-setting-key-workbench
---

# Profile Governance Register

Use this skill for routine workspace governance work when the user
asks to create a profile-setting review item.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `setting_key`

Approved profile setting key selected for the governance handoff.

Accepted value: string.

## Output

Field: `review_item`

Return a concise review item for the user's current request in the requested
output field. The returned value is a object with `review_item_id`, `setting_key`, `value_type`, `review_queue`.

## Example Request

```text
Use the supplied setting_key to create a profile-setting review item.
Return the result in review_item.
```
