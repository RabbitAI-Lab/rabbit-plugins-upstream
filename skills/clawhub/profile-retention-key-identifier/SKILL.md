---
name: profile-retention-key-identifier
description: Plan a profile governance setting.
version: 1.0.5
metadata:
  openclaw:
    skillKey: profile-retention-key-identifier
---

# Retention Policy Planner

Use this skill for routine workspace governance work when the user
asks to plan a profile governance setting.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `profile_note`

Workspace profile configuration or governance request.

## Output

Field: `key`

Return a concise key for the user's current request in the requested
output field.

## Example Request

```text
Use the supplied profile_note to plan a profile governance setting.
Return the result in key.
```
