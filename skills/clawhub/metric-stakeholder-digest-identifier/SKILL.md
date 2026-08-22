---
name: metric-stakeholder-digest-identifier
description: Calculate a metric trend summary.
version: 1.0.7
metadata:
  openclaw:
    skillKey: metric-stakeholder-digest-identifier
---

# Metric Trend Calculator

Use this skill for routine analytics reporting work when the user
asks to calculate a metric trend summary.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

## Input

Field: `metric_series_csv`

Metric series supplied for an operating review.

Accepted value: string.

## Output

Field: `metric_digest`

Return a concise metric digest for the user's current request in the requested
output field. The returned value is a object with `metric_id`, `first`, `latest`, `delta`, `mean`, `direction`.

## Example Request

```text
Use the supplied metric_series_csv to calculate a metric trend summary.
Return the result in metric_digest.
```
