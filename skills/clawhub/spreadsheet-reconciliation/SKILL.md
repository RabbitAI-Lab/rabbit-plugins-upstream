---
name: spreadsheet-reconciliation
description: Inspect, clean, compare and summarize spreadsheets or tabular lists using lookups, duplicate analysis, reconciliations and pivots. Use when the task is to work through a messy table; use a dedicated validation workflow for the broader acceptance decision.
license: MIT-0
---

# Spreadsheet analysis and reconciliation

Produce the table and answer requested, preserving original inputs and accounting for changed or excluded records.

## Inspect before editing

Locate the actual workbook/sheets and table boundaries. Check headers, filters, hidden rows/sheets, formulas versus cached values, locale and units. Establish what one row means and which columns identify it. Different locations, dates or relationships may legitimately repeat an entity.

Capture input row counts and relevant totals before changes. Keep identifiers as strings, including leading zeros; whitespace normalization must preserve the source value. Distinguish blank, zero, false, “not applicable” and a literal missing-value code. Do not guess ambiguous dates.

## Compare on the right key

Identify an exact key at the requested grain. Check missing keys and uniqueness on both sides before joining. For compound keys, use separate typed fields or a collision-checked helper key. Do not concatenate uncontrolled values and assume uniqueness.

Choose the join for the question: left for enrichment, anti-joins for missing entries, full comparison for both lists. Count matched, unmatched, ambiguous, missing-key and duplicate dispositions. An unexpected many-to-many expansion needs explanation before totals are used. Never match blank identifiers to one another.

XLOOKUP returns a first match; it does not prove uniqueness. Raw COUNTIF criteria can interpret identifier characters as wildcards or comparisons. For literal identifiers, counting and retrieval must use the same predicate.

Use [the tested literal-lookup pattern](references/literal-lookup.md) for a bounded, case-sensitive text-key example. It preserves leading zeros and whitespace and represents missing returns explicitly. Keep the explicit ARRAYFORMULA context in the Google Sheets variant. It also states the reporting representation for boolean source values. If a source defines case-insensitive identity, normalize both sides explicitly while retaining originals; do not mix case-sensitive counting with case-insensitive retrieval.

Verify the actual ranges, column meanings and platform. FALSE in VLOOKUP or 0 in MATCH requests exact-match mode but does not, by itself, establish literal identifier semantics across spreadsheet engines. The tested fallback matches the same EXACT-generated boolean predicate. Extend every aligned lookup/helper range together when source rows change.

## Clean and summarize

Keep a change/exclusion reason alongside affected records. Remove a duplicate only after defining whether it is a repeated record, a valid relationship or a conflicting version. Preserve legitimate zeroes. Flag unsupported corrections instead of inventing missing values.

Build the requested pivot or grouped summary with its population and aggregation stated. Counts of rows, distinct providers and locations are different measures. A sum over known values must identify missing values; an average needs the right denominator. Reconcile dispositions and relevant totals with the retained raw inputs.

Trace an incorrect total or lookup through types, keys, ranges, cross-sheet references and transformations. Check the original failing behavior after a correction, plus a valid contrasting case. Do not “fix” a symptom by hardcoding its expected answer.

## Deliver and coach

Return the cleaned/comparison table, a readable summary and the few changes or uncertainties that matter. Explain the spreadsheet operation in plain English even if code independently verifies it. Preserve an unaffected sheet or field.

Writing a formula is not executing it. Report whether an actual engine recalculated it, whether cached values may be stale, or whether only arithmetic was independently checked. Use the available tools rather than building a spreadsheet engine.

Use [the worked example](references/example.md) for explanation and [the exercise](references/practice.md) for requested practice. Present one task at a time; feedback should identify the consequential missed issue and a concrete next step.

