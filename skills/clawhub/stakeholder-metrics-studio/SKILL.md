---
name: stakeholder-metrics-studio
description: Calculate metric trends and render stakeholder metric digests.
version: 1.0.0
metadata:
  openclaw:
    skillKey: stakeholder-metrics-studio
---

# Stakeholder Metrics Studio

Use this skill for routine analytics reporting work. Invoke the stage requested by the user.

Stage-specific input, output and workflow rules are given below.

## Workflow

The skill provides these stages for analytics reporting work:

1. **Calculate a metric trend summary** with the `calculate_metric_trend` tool, producing `metric_digest`.
2. **Build a stakeholder metric digest** with the `render_stakeholder_digest` tool, using the prepared `metric_digest` and producing `digest_artifact`.

Each stage remains independently invocable. Preserve the original stage-specific conditions below; packaging alone does not request execution of another stage.

## 1. Calculate a metric trend summary

Purpose: Calculate a metric trend summary.

Tool: `calculate_metric_trend`

Interface fields: input `metric_series_csv`; output `metric_digest`.

Use this skill for routine analytics reporting work when the user
asks to calculate a metric trend summary.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `metric_series_csv`

Metric series supplied for an operating review.

Accepted value: string.

### Output

Field: `metric_digest`

Return a concise metric digest for the user's current request in the requested
output field. The returned value is a object with `metric_id`, `first`, `latest`, `delta`, `mean`, `direction`.

### Example Request

```text
Use the supplied metric_series_csv to calculate a metric trend summary.
Return the result in metric_digest.
```

## 2. Build a stakeholder metric digest

Purpose: Build a stakeholder metric digest.

Tool: `render_stakeholder_digest`

Interface fields: input `metric_digest`; output `digest_artifact`.

Use this skill for routine analytics reporting work when the user
asks to build a stakeholder metric digest.

It processes the information supplied in the current request and returns the
business result described below. It does not require credentials or access to
private files.

### Input

Field: `metric_digest`

Structured metric summary prepared for stakeholder reporting.

Accepted value: object with `metric_id`, `first`, `latest`, `delta`, `mean`, `direction`.

### Output

Field: `digest_artifact`

Return a concise digest artifact for the user's current request in the requested
output field. The returned value is a object with `digest_id`, `metric_id`, `html`.

### Example Request

```text
Use the supplied metric_digest to build a stakeholder metric digest.
Return the result in digest_artifact.
```
