## Description:

Helps agents query shared OneHome real-estate listings and listing details from a shell using the fpx CLI and an authorized OneHome session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate professionals use this skill to look up saved searches, shared listings, and property details through their own authorized OneHome access without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Capturing or exchanging a private OneHome session token exposes account-linked data to the CLI and browser extension.

Mitigation: Use only your own authorized session or magic-link share, and remove the fpx profile or extension access when finished.

Risk: Bearer tokens and real-estate account data may be exposed through command output, local files, or logs.

Mitigation: Treat tokens and query results as private; avoid shared machines and logs, and remove saved token files after use.

## Reference(s):

- [OneHome GraphQL and REST operations](artifact/references/graphql-operations.md)
- [ClawHub OneHome FPX release](https://clawhub.ai/chrischall/skills/onehome-fpx)
- [ContextMint Bridge extension](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance, JSON]

**Output Format:** [Markdown instructions with shell and GraphQL examples; OneHome query results in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires authorized OneHome access and a paired browser extension.]

## Skill Version(s):

1.1.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
