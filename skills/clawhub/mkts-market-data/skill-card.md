## Description:

Retrieves mkts.io market data and, with explicit user confirmation, helps manage portfolio, journal, and watchlist records for stocks, crypto, ETFs, commodities, and forex.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdliriano](https://clawhub.ai/user/sdliriano)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to query mkts.io for market data, news, screening, fundamentals, and portfolio-oriented account workflows when the user has explicitly requested them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market queries and selected portfolio, journal, or watchlist data are sent to mkts.io.

Mitigation: Send only task-relevant data, avoid secrets or unnecessary personal details, and install only when the user accepts this external-service data flow.

Risk: Portfolio, journal, and watchlist writes or deletes can persist sensitive financial records or remove records without an undo path.

Mitigation: Default to read-only behavior; before each write or delete, show the exact target and payload or affected count and obtain explicit user confirmation.

Risk: The MKTS_API_KEY credential could be exposed if printed, embedded in URLs, or stored in generated files.

Mitigation: Use MKTS_API_KEY only from the environment and only in the X-API-Key header to https://mkts.io/api/v1.

Risk: Generated portfolio card images and private API responses can reveal holdings, performance, and financial interests.

Mitigation: Confirm output destinations before writing files and do not share, export, cache, or display private responses beyond the requesting user without separate consent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdliriano/skills/mkts-market-data)
- [mkts.io API v1](https://mkts.io/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON API response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include mkts.io request details, response summaries, and user-confirmed account-operation payloads.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
