---
name: metric-stakeholder-digest
description: Combines calculate a metric trend summary with build a stakeholder metric digest.
version: 1.0.7
metadata:
  openclaw:
    skillKey: metric-stakeholder-digest
---

# Metric Trend Calculator and Stakeholder Metric Digest

Use this skill for routine analytics reporting work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Metric Trend Calculator

Tool: `calculate_metric_trend`

Reads metric series and calculates current value, change, and direction for operating reviews.

Input field: `metric_series_csv`. Metric series supplied for an operating review.

Output field: `metric_digest`.

## Operation 2: Stakeholder Metric Digest

Tool: `render_stakeholder_digest`

Builds stakeholder digests from structured metric summaries for planning and leadership updates.

Input field: `metric_digest`. Structured metric summary prepared for stakeholder reporting.

Output field: `digest_artifact`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
