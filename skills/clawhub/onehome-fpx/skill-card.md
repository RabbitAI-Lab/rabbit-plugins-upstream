## Description:

Guides agents in querying an authorized OneHome real-estate portal session from the shell using fpx to find saved searches, listings, and property details without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Real-estate agents, consumers, and developers with authorized OneHome access use this skill to retrieve saved-search listings, property details, photos, and related data through a signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Copied or captured OneHome session tokens can grant access to private portal data if exposed in files, shell history, or outputs.

Mitigation: Treat bearer tokens as account credentials; avoid shared machines and token files in /tmp, and clear shell history and temporary outputs.

Risk: Pairing browser tooling with a signed-in session may expose private portal access to tools that have not been reviewed.

Mitigation: Use only portals you are authorized to access, and review the browser extension and fpx tooling before pairing.

## Reference(s):

- [OneHome fpx skill release](https://clawhub.ai/chrischall/skills/onehome-fpx)
- [OneHome GraphQL and REST operations](references/graphql-operations.md)
- [ContextMint Bridge source and installation](https://github.com/nullnet-app/contextmint-bridge)
- [fetchproxy extension documentation](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell, GraphQL, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authorized OneHome session and a paired browser extension.]

## Skill Version(s):

1.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
