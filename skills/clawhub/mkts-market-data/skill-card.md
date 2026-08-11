## Description:

Retrieve market data and, with explicit user confirmation, manage portfolio, journal, and watchlist records through mkts.io for stocks, crypto, ETFs, commodities, and forex.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdliriano](https://clawhub.ai/user/sdliriano)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve market quotes, screen assets, review financial news and filings, compare securities, and manage mkts.io portfolio, journal, and watchlist records when the user explicitly requests those account workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial interests, portfolio records, journal notes, watchlists, and optional registration details can be sent to and stored by mkts.io.

Mitigation: Review every displayed payload before sending it, minimize personal details in notes and queries, and only submit account data after explicit user confirmation.

Risk: Account-changing operations can create, update, or delete persisted records, and the API has no documented undo for deletions.

Mitigation: Default to read-only endpoints; before POST, PATCH, or DELETE, show the exact target and payload or affected count, resolve server-generated IDs, and obtain confirmation for that exact operation.

Risk: The optional MKTS_API_KEY is a private credential for higher-rate access.

Mitigation: Use the key only from an environment variable, send it only in the X-API-Key header to https://mkts.io/api/v1, and never print, log, or store it in arbitrary files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdliriano/skills/mkts-market-data)
- [mkts.io API](https://mkts.io/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks and concise natural-language guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include curl commands, API request payloads, market summaries, and confirmation prompts for account-changing operations.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
