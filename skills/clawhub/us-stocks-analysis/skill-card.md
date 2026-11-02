## Description:

US stocks analysis by an adversarial investment committee. Legendary-investor personas independently research a thesis, attack each other's cases against a shared evidence ledger (sentiment, smart money, SEC fundamentals), and reconcile into a plain-English verdict: the bottom line first, then who disagrees and why. Structured rubrics keep every number sourced, on any model. Includes five quick data workflows. Use for stock research, investment thesis, bull case vs bear case, due diligence on a ticker, should I buy this stock, deep dive on a company. Read-only. No trading, no purchases, no write operations, no wallet access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and research users use this skill to gather read-only US equity data and produce sourced quick briefs or structured, multi-perspective thesis reviews. Its output is educational information, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stock queries and API authentication are sent to SentiSense; broad screens and committee runs can consume API quota and model costs.

Mitigation: Protect the API key and consider quotas and costs before running broad screens or debates.

Risk: Delayed or limited-preview data may provide incomplete evidence for a stock analysis.

Mitigation: Check freshness and preview limits, label partial data, and do not treat missing rows in a preview as evidence of absence.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/thesentitrader/skills/us-stocks-analysis)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense website](https://sentisense.ai)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Plain-English Markdown research briefs and investment committee verdicts with sourced evidence and caveats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ticker-based, read-only educational research; no trading or other transactions.]

## Skill Version(s):

2.10.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
