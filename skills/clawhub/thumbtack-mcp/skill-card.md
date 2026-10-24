## Description:

Helps agents search Thumbtack service providers by trade and ZIP code and read public profiles using anonymous web requests and local extraction tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find local service providers and summarize public ratings, reviews, credentials, hours, and pricing without an account or MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Anonymous shell requests reach Thumbtack and may expose sensitive inputs if private data or credentials are added.

Mitigation: Keep profile URLs on thumbtack.com; review requests before running them and do not include account cookies, credentials, or private data.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/thumbtack-mcp)
- [Thumbtack discovery recipes](references/discovery.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with shell examples and structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public provider data only; read-only lookups, no bookings or account access.]

## Skill Version(s):

1.1.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
