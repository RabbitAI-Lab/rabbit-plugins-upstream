## Description:

Helps agents query a signed-in OneHome session from a shell to find shared listings, saved searches, and listing details without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers with the account owner's consent use this skill to access their OneHome saved searches and shared property listings through a signed-in browser session without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill extracts and reuses live OneHome session credentials, which can expose account access if shared or logged.

Mitigation: Use only with the account owner's consent on a trusted, single-user machine; do not log authorization headers and unset bearer-token variables after use.

Risk: The provided temporary-file examples can leave token-bearing data accessible or retained.

Mitigation: Use private temporary files instead of the examples as written, and delete token-bearing data immediately after use.

## Reference(s):

- [OneHome GraphQL and REST operations](artifact/references/graphql-operations.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell and GraphQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands retrieve account-scoped OneHome data as JSON when run.]

## Skill Version(s):

1.1.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
