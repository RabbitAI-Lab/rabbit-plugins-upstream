---
name: metric-stakeholder-digest-workbench
description: Build a stakeholder metric digest.
version: 1.0.7
metadata:
  openclaw:
    skillKey: metric-stakeholder-digest-workbench
---

# Stakeholder Metric Digest

Use this skill for routine analytics reporting work when the user
asks to build a stakeholder metric digest.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `metric_digest`

Structured metric summary prepared for stakeholder reporting.

Accepted value: object with `metric_id`, `first`, `latest`, `delta`, `mean`, `direction`.

## Output

Field: `digest_artifact`

Return a concise digest artifact for the user's current request in the requested
output field. The returned value is a object with `digest_id`, `metric_id`, `html`.

## Example Request

```text
Use the supplied metric_digest to build a stakeholder metric digest.
Return the result in digest_artifact.
```
