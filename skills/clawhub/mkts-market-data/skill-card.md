## Description:

Retrieve market data and, with explicit user confirmation, manage portfolio, journal, and watchlist records through mkts.io for stocks, crypto, ETFs, commodities, and forex.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdliriano](https://clawhub.ai/user/sdliriano)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to retrieve market quotes, screen assets, review financial news and fundamentals, and manage portfolio, journal, or watchlist records when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market queries and confirmed portfolio, journal, or watchlist details are sent to mkts.io.

Mitigation: Install only when that external data sharing is acceptable, minimize submitted personal details, and avoid including secrets in notes or natural-language requests.

Risk: Authenticated write or delete actions can change persisted portfolio, journal, or watchlist records.

Mitigation: Review the exact displayed payload or target record and require explicit user confirmation immediately before each write or delete.

Risk: MKTS_API_KEY is a credential for higher limits and authenticated account workflows.

Mitigation: Provide it only through an environment variable and send it only as the X-API-Key header to https://mkts.io/api/v1.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdliriano/skills/mkts-market-data)
- [mkts.io API base URL](https://mkts.io/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses curl and optional MKTS_API_KEY for higher rate limits and authenticated account workflows.]

## Skill Version(s):

1.0.17 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
