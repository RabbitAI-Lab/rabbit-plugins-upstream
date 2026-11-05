---
name: data-quality-measurement
description: Define and calculate dataset quality metrics, sampling plans and uncertainty, including completeness, verified correctness, coverage, precision and recall. Use for measurement questions rather than the whole delivery-acceptance or vendor-investment decision.
license: MIT-0
---

# Data-quality measurement

Choose a measure that supports the intended customer action. A convenient statistic is not automatically a useful quality measure.

## Define before calculating

State the unit (field, record, relationship or entity), eligible population/time window, correctness rule, numerator, denominator, missing/unverified policy and source of truth. A formatting rule is not a factual reference. Distinguish required fields from optional or inapplicable fields.

Keep separate:
- Completeness: populated eligible required values / eligible required values.
- Verified correctness: verified correct values / independently assessed values, with the unverified count and assessed fraction shown.
- Coverage: represented eligible entities / a defensible target population. State whether representation also requires usable, correct data.
- Precision: true positives / all predicted positives.
- Recall: true positives / all relevant positives, including misses.

Do not estimate recall from accepted predictions alone, or coverage without a defensible population. Missing labels are not automatically errors, successes or negative examples. Define how abstentions affect each denominator. Record counts are not unique-entity counts.

## Sample for a decision

Determine whether the task is finding defects or estimating a population rate. Inspect available population strata such as specialty, geography, source, entity type and freshness. A vendor-selected sample is not automatically representative.

Choose sample size and selection based on the uncertainty or defect rate that matters, expected heterogeneity, cost and available ground truth. A small sample can diagnose problems without establishing a precise population estimate. Do not turn 50–100 records or 95% accuracy into universal requirements.

For a population estimate, document selection probabilities and use appropriate weights when sampling strata disproportionately. Show subgroup performance when failures matter there. Clustered records and repeated providers can violate independence; do not use a simple binomial interval as though those rows were independent.

For independent random Bernoulli observations, a Wilson interval or exact binomial method is preferable to a naive normal interval near zero errors or a small sample. State the confidence level, assumptions and method; use verified software/arithmetic rather than inventing an interval. Zero observed defects is not proof of zero population defects. An interval cannot repair a biased sample.

## Interpret and monitor

Explain whether the observed error could change the customer action. Set a threshold from a supplied decision requirement or clearly label a proposal and tradeoff. Preserve a critical subgroup defect even when the overall rate looks strong.

Compare like populations and versions over time. Separate source-data changes, collection failure, label-rule changes and actual model deterioration. Define cadence from update behavior and error consequence. A failed retrieval is an availability observation, not proof of changed truth.

Return the measure definition, counts, estimate/uncertainty, main failure patterns and a supported next action. Stop when the assigned question is answered; do not replace a metric request with an entire quality platform.

For a worked calculation read [example](references/example.md). Use [practice](references/practice.md) for requested coaching; explain feedback from actual arithmetic and definitions.

