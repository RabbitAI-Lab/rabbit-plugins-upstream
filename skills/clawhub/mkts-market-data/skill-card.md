## Description:

Retrieves market data through mkts.io and, with explicit user confirmation, manages portfolio, journal, and watchlist records for stocks, crypto, ETFs, commodities, and forex.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdliriano](https://clawhub.ai/user/sdliriano)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to retrieve quotes, market overviews, historical prices, news, screeners, and related market research, and to perform user-confirmed portfolio, journal, and watchlist workflows through mkts.io.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market queries and any chosen portfolio, journal, or watchlist data are sent to mkts.io and may include sensitive financial interests.

Mitigation: Use the skill's documented data minimization guidance, avoid unnecessary personal data, and disclose the external transmission before account workflows.

Risk: Portfolio, journal, and watchlist mutations can persist account data or delete records without a documented undo.

Mitigation: Display the exact target and payload or affected count, resolve server-generated IDs before deletion, and obtain explicit confirmation immediately before each mutation.

Risk: The optional MKTS_API_KEY credential could be exposed if printed, embedded in URLs or bodies, or stored insecurely.

Mitigation: Use MKTS_API_KEY only from an environment variable and send it only in the X-API-Key header to https://mkts.io/api/v1.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdliriano/skills/mkts-market-data)
- [Publisher profile](https://clawhub.ai/user/sdliriano)
- [mkts.io API base](https://mkts.io/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl command examples and JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call external mkts.io endpoints; portfolio, journal, watchlist, registration, and AI query workflows require explicit user confirmation where documented.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
