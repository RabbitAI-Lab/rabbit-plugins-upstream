---
name: service-capacity-window-identifier
description: Select a service capacity window.
version: 1.0.7
metadata:
  openclaw:
    skillKey: service-capacity-window-identifier
---

# Service Capacity Window Planner

Use this skill for routine service capacity planning work when the user
asks to select a service capacity window.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `capacity_request`

Date, time, and timezone requested for a service capacity reservation.

Accepted value: object with `date`, `time`, `timezone`.

## Output

Field: `capacity_window`

Return a concise capacity window for the user's current request in the requested
output field. The returned value is a date-time.

## Example Request

```text
Use the supplied capacity_request to select a service capacity window.
Return the result in capacity_window.
```
