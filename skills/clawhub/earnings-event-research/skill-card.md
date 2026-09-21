## Description:

Build sourced pre- or post-earnings briefs through Crawlora by joining Yahoo Finance event, estimate, reported-result, and daily-price data with SEC filings and normalized financials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, finance teams, and developers use this skill to produce traceable earnings previews or recaps that combine Yahoo Finance earnings data, SEC filings, normalized financials, and defined price windows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User finance queries and the Crawlora API key are sent to Crawlora.

Mitigation: Use a dedicated Crawlora API key and avoid private or unnecessary sensitive data in query parameters.

Risk: Calendar rows, earnings modules, SEC filings, normalized financials, and daily prices can be missing, stale, revised, or internally inconsistent.

Mitigation: Preserve source timestamps, issuer identifiers, filing accession, calculation formulas, uncertainty, and material gaps.

Risk: Daily price windows can show association around an earnings event, not causality or intraday reaction.

Mitigation: State the exact price-window formula and trading dates, and do not turn the research brief into a buy or sell call.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora skill page](https://clawhub.ai/crawlora-org/skills/earnings-event-research)
- [Crawlora](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown research brief with sourced calculations, evidence ledger, and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses bounded GET requests to Crawlora finance and SEC data endpoints.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
