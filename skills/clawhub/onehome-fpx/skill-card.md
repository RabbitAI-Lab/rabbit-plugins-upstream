## Description:

Query OneHome (CoreLogic), the agent magic-link real-estate portal at portal.onehome.com, from a shell with the fpx CLI instead of running the onehome-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically capable real-estate users use this skill to access authorized OneHome saved-search and listing data from shell workflows without installing or running the onehome-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill operationalizes OneHome magic-link or browser session credentials, which can expose sensitive account, contact, MLS, or listing data if mishandled.

Mitigation: Use only accounts and property shares you are authorized to access, avoid shared machines, do not log or commit tokens or temporary outputs, and remove temporary files containing session or listing data.

Risk: Some OneHome fields and operations are agent-only and may return access errors for consumer-share sessions.

Mitigation: Prefer the consumer-readable saved-search path first and check GraphQL error responses before using returned data.

## Reference(s):

- [OneHome GraphQL + REST operations for fpx](references/graphql-operations.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell, GraphQL, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may involve temporary files and bearer-token handling for authorized OneHome sessions.]

## Skill Version(s):

0.14.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
