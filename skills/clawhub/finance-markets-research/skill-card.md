## Description:

Researches stocks, crypto, SEC filings, insider/congressional trading, and private-market profiles via the Crawlora API, returning clean JSON for finance and market research tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to retrieve normalized finance, market, filing, trading-disclosure, crypto, and private-market data for research workflows. It helps agents choose Crawlora endpoints and compose API calls for ticker lookups, SEC filings, congressional trades, crypto market data, and private-company or fund profiles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call Crawlora endpoints beyond the stated finance research scope and can send arbitrary request bodies.

Mitigation: Review calls before execution and restrict use to finance, SEC, congressional-disclosure, crypto, and private-market endpoints needed for the task.

Risk: Finance and company research queries are sent to the Crawlora API.

Mitigation: Avoid sending confidential or sensitive research prompts, tickers, entities, or payloads unless that use is approved.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY and sends research queries to Crawlora.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
