---
name: mx-data
description: Use this skill for authoritative Eastmoney MX financial data lookups when the user asks for exact, time-sensitive market or company data such as real-time quotes, historical prices, capital flows, valuation metrics, financial statements, company basics, shareholders, executives, or entity relationships. Do not use for news/reports/announcements (use mx-search), condition-based stock screening (use mx-xuangu), watchlist actions (use mx-zixuan), or simulated trading operations (use mx-moni).
---

# mx-data

Use `mx_data.py` to query Eastmoney MX data through natural language and produce structured Excel/JSON outputs.

## Trigger Boundaries

- Use for exact data questions: price, close/open/high/low, volume, turnover, PE/PB, ROE, revenue, profit, balance sheet items, dividends, shareholders, executives, company profile, sector/index/fund quotes.
- Prefer this skill whenever the answer depends on current or historical market data rather than model memory.
- Do not use it for event interpretation, news causality, announcements, research reports, policy text, or market narrative; use `mx-search` first for those.
- Do not use it to screen a universe by constraints such as "ROE > 15%" or "PE < 20"; use `mx-xuangu`.

## Inputs

- Required: a clear natural-language query with entity, metric, and time range or date.
- Ask a concise follow-up if the entity, metric, or period is ambiguous and the ambiguity changes the result.
- Use narrower periods for daily-level data. Multi-year daily queries can create large Excel/JSON files and overload context.
- Require `MX_APIKEY` in the environment. Optional: set `MX_OUTPUT_DIR`; otherwise output goes to `~/.codex/skills-output/mx_data/output`.

## Workflow

1. Normalize the user request into one focused query. Include the entity code/name, metric, market if needed, and date range.
2. Run:

```bash
python /Users/lu/.codex/skills/mx-data/mx_data.py "贵州茅台近三年净利润 营业收入"
```

3. Inspect the terminal preview first. Open generated Excel/JSON only when deeper parsing is needed.
4. If the raw JSON shape matters, load `references/result-fields.md`.
5. Answer with the data source, query used, time range, key values, and generated file paths when files were created.

## Output Contract

- State that the data came from Eastmoney MX via `mx-data`.
- Include units, dates, and whether values are real-time, daily, annual, or another granularity.
- For tables, summarize the important rows/columns and point to the generated `.xlsx` and `_raw.json`.
- Do not turn raw data into investment advice unless the user explicitly asks for analysis; even then, distinguish data from judgment.

## Failure Handling

- Missing `MX_APIKEY`: ask the user to configure it; do not invent values.
- Empty result: broaden entity/metric wording or reduce condition specificity.
- Large output: rerun with a narrower time range or fewer metrics.
- API limit/auth errors: report the code and stop.
- Network/JSON errors: retry once only if the failure looks transient; otherwise report the failure and preserve any raw output path.

## Validation

- Use `evals/evals.json` after changing this skill or its script.
- Positive cases should trigger `mx-data`; adjacent news, screening, watchlist, and trading prompts should not.
