---
name: ctr-json-normalizer
description: Normalize the final JSON output of a single-session CTR product-card click diagnosis. Use after the diagnosis draft is complete and before replying, whenever the report must contain exactly the agreed query, clicked item, unclicked items, five fixed dimensions, structured suggestions, and limitations.
---

# CTR JSON Normalizer

Run this Skill once as the final step of every CTR diagnosis. It formats and validates a completed diagnosis; it does not fetch images, compare products, infer causes, or write new business suggestions.

## Input

Pass one JSON object through stdin:

```json
{
  "session": { "query": "", "clicked_item_id": "", "items": [] },
  "report": { }
}
```

`report` may be a JSON object or a JSON string. `session.items` must be the original card list, with `item_id`, `position`, and `clicked` where available.

## Run

```bash
python3 scripts/normalize_ctr_report.py <<'JSON'
{ "session": { "query": "...", "clicked_item_id": "...", "items": [] }, "report": {} }
JSON
```

## Required Workflow

1. Finish all comparison and image-fact collection first.
2. Build the diagnosis draft as JSON, using evidence already collected.
3. Run `scripts/normalize_ctr_report.py` with the original session and the draft.
4. If it returns `error`, fix the draft JSON and run it again.
5. Return the script stdout verbatim. Do not wrap it in Markdown or append explanatory text.

The script fixes only the report envelope: root fields, candidate item coverage, dimension order, allowed status values, suggestion field shape, and limitations. A missing dimension becomes `unknown` with no suggestion; no factual claim is invented.
