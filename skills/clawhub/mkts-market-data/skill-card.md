## Description:

Retrieve market data for stocks, crypto, ETFs, commodities, and forex through mkts.io, and with explicit user confirmation manage portfolio, journal, and watchlist records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdliriano](https://clawhub.ai/user/sdliriano)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and financial research agents use this skill to retrieve quotes, screen assets, compare tickers, read market news and fundamentals, and manage user-requested portfolio, journal, and watchlist records through mkts.io.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send market queries, request bodies, request metadata, and authenticated API keys to the external mkts.io service.

Mitigation: Use MKTS_API_KEY only from an environment variable, send it only in the X-API-Key header to the mkts.io API, and avoid unnecessary personal or secret information in requests.

Risk: Portfolio, journal, and watchlist mutations can persist sensitive financial interests to the API-key owner's account.

Mitigation: Default to read-only endpoints and require explicit user confirmation of the exact target and payload before every POST, PATCH, or DELETE.

Risk: Delete operations may remove account records without a documented undo path.

Mitigation: Resolve the exact server-generated ID or affected clear-all count with a matching GET request, show it to the user, warn that no undo is documented, and confirm immediately before deletion.

Risk: Portfolio card images and private API responses can expose private portfolio data.

Mitigation: Generate portfolio images only on user request, confirm the destination path, avoid overwriting files without confirmation, and do not share private responses or images without separate consent.

## Reference(s):

- [mkts.io API base URL](https://mkts.io/api/v1)
- [ClawHub skill listing](https://clawhub.ai/sdliriano/skills/mkts-market-data)
- [Publisher profile](https://clawhub.ai/user/sdliriano)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Text]

**Output Format:** [Markdown with inline bash code blocks and endpoint summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON API responses from mkts.io or an image file when the user explicitly requests the portfolio card endpoint.]

## Skill Version(s):

1.0.18 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
