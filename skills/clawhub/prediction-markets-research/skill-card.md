## Description:

Pulls prediction-market odds, order books, price history, and forecast questions from Polymarket, Kalshi, and Metaculus via the Crawlora API as JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and researchers use this skill to query prediction-market and forecasting data for odds checks, order books, price history, and community forecasts without directly scraping the source platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the user's Crawlora API key and requested prediction-market questions or identifiers to Crawlora.

Mitigation: Install only if this data sharing is acceptable; keep the API key in CRAWLORA_API_KEY and do not hardcode or commit it.

Risk: Prediction-market odds and community forecasts can be volatile, incomplete, or unsuitable as financial advice.

Mitigation: Treat returned market data as research input, verify important results against source platforms or other evidence, and avoid using the skill for trading or account actions.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/prediction-markets-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and returns data from supported read-only endpoints.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
