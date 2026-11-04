# Worked example: compare clinician contacts

Synthetic data. Left list is one row per clinician/location.

| Clinician | Location | Volume |
| --- | --- | --- |
| C71 | R2 | 40 |
| C72 | R3 | 15 |
| C72 | R4 | 25 |
| C72 | R3 | 15 |

The roster contains C71/R2 as cardiology and C72/R3 and C72/R4 as orthopedics. The last left row exactly repeats C72/R3.

Keep the two different C72 locations. Retain the original, exclude the exact repeated record from the comparison and document why. The raw known-volume total is 95; removing the repeated 15 gives 80 across three clinician/location rows.

Use a compound clinician/location key whose construction cannot collide. Check roster key uniqueness before an exact lookup. A grouped summary of the matched rows is cardiology: 1 location and volume 40; orthopedics: 2 locations and volume 40. There are two distinct clinicians, not three.

In Excel or Sheets, add a checked key and match-status column, then create a pivot with specialty as rows and sum of volume and count of location as values. A distinct-clinician measure requires a distinct-count method or a separately deduplicated clinician table.

These values were derived arithmetically; this example does not claim an executed workbook formula.

For executable formulas rather than a conceptual pivot example, use [the literal-key lookup pattern](literal-lookup.md). It checks duplicates with the same identity predicate as retrieval and keeps missing values distinct from zero.
