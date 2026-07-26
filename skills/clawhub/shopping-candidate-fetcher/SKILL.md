---
name: shopping-candidate-fetcher
description: Fetch structured shopping candidate lists from pre-collected shopping platform screenshot snapshots. Use this skill when a user asks for product options and the final selection should be made by the downstream shopping agent.
---

# shopping-candidate-fetcher

Use this skill as a candidate-retrieval layer over the local shopping snapshot dataset.

Do not use this skill as a live shopping search engine.
Do not use this skill as the final recommender.

## Workflow

1. Judge whether the task needs a candidate pool for a shopping request.
2. Check `data/query_index.json` to find a supported snapshot query.
3. Run `scripts/fetch_candidate_list.py` with a supported query and a positive `top_k`.
4. Return the structured candidate list as retrieval output.
5. Perform any ranking, filtering, recommendation, or final selection outside this skill.

## Match the query

- Prefer an exact query string that already exists in `data/query_index.json`.
- If the user's wording differs but clearly matches one indexed query, reuse the indexed query and say which snapshot query was used.
- If no indexed query is close enough, do not invent candidates. Explain that the local snapshot dataset does not yet cover the request.

## Run the script

Prefer the bundled script over manual JSON assembly.

```powershell
python scripts/fetch_candidate_list.py --query "我想买一双适合日常慢跑的舒适跑鞋。" --top-k 5
```

Use `top_k=5` unless the user asks for a different number.
Keep `top_k` greater than `0`.

The script:

- loads `data/query_index.json`
- resolves the mapped file in `data/snapshots/`
- reads the snapshot JSON
- returns the first `top_k` entries from `candidates`

## Output contract

Preserve the returned structure. Treat it as the source-of-truth retrieval payload.

Top-level fields currently include:

- `skill_name`
- `skill_version`
- `source`
- `query_id`
- `query`
- `search_keyword`
- `source_platform`
- `capture_method`
- `screenshot_file`
- `capture_date`
- `top_k`
- `candidates`

Each candidate currently includes fields such as:

- `rank`
- `item_id`
- `title`
- `brand`
- `price`
- `sales_text`
- `rating`
- `shop`
- `location`
- `description`
- `url`
- `is_ad`

Do not rename fields unless you are intentionally changing the code and all downstream consumers.
Do not add final-decision fields such as `selected_item_id`, `must_choose`, or recommendation labels inside the raw retrieval payload.

## Data expectations

- Treat this dataset as static snapshot data, not real-time marketplace data.
- Use `capture_date` and `source_platform` as provenance metadata when explaining freshness.
- Expect `rating`, `url`, or `sales_text` to be missing or `null` for some items because the source is screenshot-derived.
- Prefer the cleaned snapshot JSON in `data/snapshots/` for structured output.
- The public package retains cleaned JSON snapshots. Original screenshot images are not required for normal execution and may be omitted from the repository.

## Failure handling

- If `query` is empty, expect a `ValueError`.
- If `top_k <= 0`, expect a `ValueError`.
- If the query is not present in `data/query_index.json`, do not fabricate a result. Report that no clean snapshot exists for the request.
- If a mapped snapshot file is missing, verify the filename in `data/query_index.json` and the corresponding file under `data/snapshots/`.

## Maintain the dataset

To support a new shopping request:

1. Add a new query-to-file mapping in `data/query_index.json`.
2. Add the corresponding cleaned snapshot JSON to `data/snapshots/`.
3. Keep the snapshot schema aligned with the existing files.

Use the keys in `data/query_index.json` as the canonical supported query phrasings.
