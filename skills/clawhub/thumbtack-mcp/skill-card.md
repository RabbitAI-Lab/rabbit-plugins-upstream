## Description:

Query thumbtack.com from a shell to search local service professionals by trade and zip code and read public professional profiles with ratings, reviews, credentials, business hours, and pricing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to compose curl, jq, and Node-based workflows for retrieving public Thumbtack search results and professional profile data without an MCP server, login, API key, or browser extension.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes anonymous network requests to Thumbtack pages and its GraphQL endpoint.

Mitigation: Use it only for public consumer search and profile data, avoid credentials or private account data, and consider Thumbtack terms and rate limits.

Risk: Thumbtack page structures, JSON stores, and GraphQL response shapes can vary or change.

Mitigation: Check extractor exits and GraphQL errors, follow the documented page-type rules, and branch on optional or union fields such as pricing.

Risk: The bundled Node extractor parses returned HTML locally.

Mitigation: Review the artifact before installation and run it with least privilege on public Thumbtack HTML only.

## Reference(s):

- [Thumbtack discovery recipes](artifact/references/discovery.md)
- [Thumbtack consumer site](https://www.thumbtack.com)
- [Thumbtack anonymous GraphQL endpoint](https://app.thumbtack.com/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/thumbtack-mcp)

## Skill Output:

**Output Type(s):** [markdown, shell commands, code, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands, jq projections, and JSON extraction output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a bundled local Node extractor that reads HTML from stdin and writes JSON to stdout.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
