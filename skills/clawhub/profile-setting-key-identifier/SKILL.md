---
name: profile-setting-key-identifier
description: Choose a profile setting key.
version: 1.0.7
metadata:
  openclaw:
    skillKey: profile-setting-key-identifier
---

# Profile Setting Directory

Use this skill for routine workspace governance work when the user
asks to choose a profile setting key.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `profile_request`

Workspace request category used to locate the relevant profile setting.

Accepted value: object with `request_kind`.

## Output

Field: `setting_key`

Return a concise setting key for the user's current request in the requested
output field. The returned value is a string.

## Example Request

```text
Use the supplied profile_request to choose a profile setting key.
Return the result in setting_key.
```
