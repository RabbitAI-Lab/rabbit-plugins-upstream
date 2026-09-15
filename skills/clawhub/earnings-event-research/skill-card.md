## Description:

Build sourced earnings-event research briefs by joining Crawlora Yahoo Finance event, estimate, reported-result, and price data with SEC filings and normalized financials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to prepare earnings previews, earnings-surprise checks, fiscal-period comparisons, and bounded post-results reaction briefs. It helps keep event timing, estimates, reported values, SEC evidence, price windows, calculations, and material gaps separate and traceable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticker/company queries, date ranges, and the Crawlora API key are sent to Crawlora.

Mitigation: Use a dedicated Crawlora key, keep it out of logs and committed files, and avoid submitting sensitive or restricted research queries.

Risk: Earnings data, filings, and price windows can be stale, revised, incomplete, or internally inconsistent.

Mitigation: Preserve retrieval time and source fields, report conflicts and material gaps, and review results as research evidence rather than trading advice.

Risk: Daily price changes around earnings can be mistaken for causal market reactions.

Mitigation: State the exact price-window formula and trading dates, and avoid presenting associated price movement as proof of causality.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/earnings-event-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown research brief with sourced calculations and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include issuer identity, event timing, estimate baseline, reported metrics, SEC filing evidence, price-window definition, calculations, retrieval time, and material gaps.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
