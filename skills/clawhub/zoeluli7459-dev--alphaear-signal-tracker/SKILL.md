---
name: alphaear-signal-tracker
description: Use this skill to track the evolution of an existing finance or investment signal when the user provides a prior thesis/signal and asks whether new market information strengthens, weakens, falsifies, realizes, or leaves it unchanged. It should compare baseline logic with updated news, prices, and fundamentals, then output a structured signal update. Use mx-search and mx-data for fresh facts as needed; do not use for simple news lookup, raw data lookup, stock screening, or diagram-only requests.
---

# AlphaEar Signal Tracker

Track whether new market information changes an existing investment signal.

## Inputs

- Required: baseline signal or thesis, plus new event/time window or a request to refresh latest information.
- Preferred baseline fields: title, affected tickers, transmission chain, expected catalyst, timeframe, confidence, sentiment, and falsification conditions.
- If no baseline signal exists, first build one from the user's thesis and label assumptions clearly.

## Workflow

1. Parse the baseline signal: thesis, affected tickers, expected mechanism, time horizon, and falsification criteria.
2. Gather fresh facts:
   - Use `mx-search` for news, announcements, reports, policy, and event context.
   - Use `mx-data` for price, volume, financial metrics, and other exact data.
3. Compare new information with each baseline logic node.
4. Classify evolution as `Strengthened`, `Weakened`, `Falsified`, `Realized`, or `Unchanged`.
5. Update confidence, sentiment, expectation gap, and affected tickers only when evidence supports it.
6. Use `references/PROMPTS.md` for the research, analysis, and tracking prompt patterns when generating strict signal JSON.

## Output Contract

- Start with the evolution label and one-sentence reason.
- Include evidence grouped by news/event, price/data, and logic-chain impact.
- Show what changed from the baseline and what did not.
- Return structured JSON when the downstream workflow needs `InvestmentSignal`; otherwise provide a compact human-readable update.
- Separate facts from inference and state unresolved uncertainties.

## Failure Handling

- Missing baseline: ask for the prior signal or create an explicitly provisional baseline.
- No fresh data: state that evidence is insufficient and do not change the signal.
- Conflicting evidence: mark mixed impact and explain which logic nodes conflict.
- Data/search failures: report the failed source and avoid filling gaps from memory.

## Validation

- Run or review `tests/test_tracker.py` after changing scripts.
- Use `evals/evals.json` to ensure tracker prompts trigger this skill while simple search/data/diagram prompts route elsewhere.
