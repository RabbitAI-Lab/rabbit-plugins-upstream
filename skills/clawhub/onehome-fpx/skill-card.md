## Description:

Query OneHome saved searches and listings from a shell using fpx and a signed-in browser session without running the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate agents use this skill to access their authorized OneHome saved searches, shared listings, and listing details from a shell without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Magic-link tokens and session credentials can expose OneHome account access if captured in command output, logs, history, or temporary response files.

Mitigation: Treat tokens and authorization headers as secrets; avoid sharing logs or history and delete temporary token files after use.

Risk: The browser-pairing workflow grants the fpx CLI and ContextMint Bridge access to the signed-in session.

Mitigation: Verify the CLI and browser extension source before pairing the browser.

## Reference(s):

- [OneHome fpx release](https://clawhub.ai/chrischall/skills/onehome-fpx)
- [OneHome GraphQL and REST operations](artifact/references/graphql-operations.md)
- [ContextMint Bridge extension](https://github.com/nullnet-app/contextmint-bridge)
- [fpx extension documentation](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, GraphQL queries]

**Output Format:** [Markdown with shell and GraphQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries return OneHome data subject to the signed-in user's access; check responses for GraphQL errors.]

## Skill Version(s):

1.1.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
