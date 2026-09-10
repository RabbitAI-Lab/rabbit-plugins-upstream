## Description:

OpenNews helps agents retrieve real-time crypto, equities, macro, and financial-market news from the OpenNews 6551 API, including source filters, AI ratings, trading signals, and bilingual summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[infra403](https://clawhub.ai/user/infra403)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, analysts, and market-research agents use OpenNews to query financial news, market signals, strategy events, company reports, and disclosure evidence through documented REST and WebSocket calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OPENNEWS_TOKEN may be exposed when used in a WebSocket query string or copied into logs and shared command histories.

Mitigation: Prefer REST calls that pass the token in the Authorization header, avoid logging token-bearing URLs, and rotate the token if it may have appeared in a URL.

Risk: The package declares generic local read capability even though the documented workflows are primarily API calls.

Mitigation: Limit runtime permissions to the documented curl/API workflows unless local file access is explicitly needed and reviewed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/infra403/skills/opennews-mcp)
- [Publisher Profile](https://clawhub.ai/user/infra403)
- [OpenNews Token Registration](https://6551.io/mcp)
- [OpenNews API Base URL](https://ai.6551.io)
- [Strategy Management](https://www.newsliquid.com/strategy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Configuration guidance]

**Output Format:** [Markdown guidance with curl commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some workflows require OPENNEWS_TOKEN; free endpoints are available with limited search capabilities.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
