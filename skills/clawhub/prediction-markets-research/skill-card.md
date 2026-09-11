## Description:

Pulls prediction-market odds, order books, and forecast questions from Polymarket, Kalshi, and Metaculus via the Crawlora API as clean JSON for market-odds and forecasting research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and researchers use this skill to query current and historical prediction-market data, compare odds across platforms, inspect order books and price history, and retrieve community forecast aggregates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key and sends prediction-market search queries or JSON request bodies to Crawlora.

Mitigation: Use a scoped Crawlora key where available, provide it only through CRAWLORA_API_KEY, avoid sending sensitive research prompts or private data, and rotate the key if exposure is suspected.

Risk: Server security review reports that the API helper is broader than the documented read-only market-data purpose requires.

Mitigation: Review the helper before deployment and restrict use to documented prediction-market routes and HTTP methods.

Risk: Prediction-market data and community forecasts can be incomplete, stale, volatile, or misleading.

Mitigation: Treat outputs as research signals rather than financial advice, verify important claims against primary market pages, and disclose uncertainty when summarizing results.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/prediction-markets-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends market-search queries or JSON request bodies to Crawlora.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
