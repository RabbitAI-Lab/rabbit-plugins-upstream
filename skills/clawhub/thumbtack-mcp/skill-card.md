## Description:

Helps agents search Thumbtack for local service professionals and read public profiles, reviews, credentials, hours, and pricing using anonymous shell requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to find local service professionals by trade and ZIP code and summarize public Thumbtack profile details without signing in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shell commands make anonymous network requests to Thumbtack, and unchecked profile URLs or query files could target unintended content.

Mitigation: Keep profile URLs on Thumbtack pages and review generated GraphQL and query files before reusing them.

## Reference(s):

- [Thumbtack discovery recipes](references/discovery.md)
- [thumbtack-mcp release](https://clawhub.ai/chrischall/skills/thumbtack-mcp)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only guidance for public search results and professional profiles.]

## Skill Version(s):

1.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
