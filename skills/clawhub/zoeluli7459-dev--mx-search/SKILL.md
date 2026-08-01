---
name: mx-search
description: Use this skill for finance-specific information retrieval with Eastmoney MX search when the user asks for time-sensitive or source-backed financial news, announcements, research reports, policies, trading rules, market events, event explanations, or impact analysis. Prefer it over generic web search for China/A-share finance information. Do not use for exact quote/financial statement data (use mx-data), condition-based stock screening (use mx-xuangu), watchlist actions (use mx-zixuan), or simulated trading operations (use mx-moni).
---

# mx-search

Use `mx_search.py` to retrieve finance news and event context from Eastmoney MX selected sources.

## Trigger Boundaries

- Use for "latest", "today", "recent", "why did it move", announcements, research reports, policy updates, trading rules, event timelines, and source-backed market explanations.
- Use before analysis when the user asks about a specific finance event whose facts may have changed.
- Do not use for pure numerical quote/financial data; call `mx-data`.
- Do not use for stock universe filtering; call `mx-xuangu`.

## Inputs

- Required: event/topic/entity plus what kind of source is needed if known, such as announcement, research report, policy, or news.
- Ask a follow-up only when missing entity/time/source type would likely retrieve the wrong event.
- Require `MX_APIKEY`. Optional: set `MX_OUTPUT_DIR`; otherwise output goes to `~/.codex/skills-output/mx_data/output`.

## Workflow

1. Rewrite the user request into a search query with entity, event, date window if known, and source preference.
2. Run:

```bash
python /Users/lu/.codex/skills/mx-search/mx_search.py "贵州茅台最新研报 机构观点"
```

3. Read terminal results for title, source, date, and content trunk.
4. Load the generated `.txt` for longer extracted content or `.json` when metadata matters.
5. If source ranking or result fields are unclear, read `references/result-fields.md`.

## Output Contract

- Cite source names and dates from the returned results.
- Separate facts, source claims, and your inference.
- For impact analysis, state the transmission logic and uncertainty instead of presenting source snippets as certainty.
- Include generated file paths when useful for audit.

## Failure Handling

- Missing `MX_APIKEY`: stop and ask the user to configure it.
- Sparse results: broaden the query or try the official name/code of the entity.
- Conflicting sources: present the conflict and prefer official announcements or exchange/company disclosures where available.
- API limit/auth/network errors: report the exact issue and do not fill gaps from memory.

## Validation

- Use `evals/evals.json` after changing routing or output behavior.
- When changing the description, add both positive trigger examples and near-miss negative examples.
