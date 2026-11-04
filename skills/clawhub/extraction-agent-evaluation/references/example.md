# Worked example: trials at facilities

Synthetic source: study X10 is at campus B60 and study X20 at campus B61. Define exact IDs, supported device/status fields, dates and a source location per essential fact.

An output with X10 at B99 and invented X30 has valid JSON, but it has a wrong affiliation, one omitted record and one unsupported record. With IDs aligned, record precision and recall are each 1/2. Those metrics do not establish that the matched record's fields are correct.

A source pointer for X10 cannot ground X20's facility even if X20's facility value happens to be correct. Record source support separately. Preserve false and zero as real values; an optional count may be unknown without implying zero.

For the small flat contract used by the optional scorer, run:
```sh
python3 scripts/score_flat_records.py gold.json predicted.json
```
Fields are id, facility, device, status, active, optional count and source. Active is an explicit administrative boolean, independent of status. This scorer does not process PDFs or score arbitrary nested JSON; define appropriate field rules for a different contract.
