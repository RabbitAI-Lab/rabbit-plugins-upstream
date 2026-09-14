## Description:

Pulls prediction-market odds, order books, and forecast questions from Polymarket, Kalshi, and Metaculus via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research current and historical prediction-market signals, including odds, order books, price history, and forecast-community aggregates for events across Polymarket, Kalshi, and Metaculus.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches, requested market identifiers, and API credentials are sent to Crawlora.

Mitigation: Use a dedicated Crawlora API key, keep it in the environment, and avoid sending sensitive event research queries.

Risk: Market odds and forecast aggregates can be mistaken for financial advice.

Mitigation: Treat returned data as research input and independently review market context before making decisions.

Risk: Large Polymarket token batches can exceed documented request limits.

Mitigation: Chunk Polymarket token batch requests to 25 ids or fewer per call.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/prediction-markets-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are read-only market research data; API responses may require downstream JSON inspection or summarization.]

## Skill Version(s):

1.0.16 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
