## Description:

Guides agents to search public Etix events, venues, and performers and retrieve event and venue details through the fpx browser bridge instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to find public Etix events and venues from shell workflows without running the Etix MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser bridge grants fetch access and retains a local fpx pairing.

Mitigation: Limit the bridge profile to etix.com, verify the extension and package sources, and review the persistent pairing before installation.

Risk: Use in a logged-in session could expose account or purchase actions beyond public event lookup.

Mitigation: Restrict use to anonymous Etix discovery; do not use the skill for purchases or logged-in account actions.

## Reference(s):

- [Etix consumer endpoints and extraction recipes](references/etix-endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [fetchproxy extension setup](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell commands and public event or venue data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public discovery only; no purchasing or logged-in account actions.]

## Skill Version(s):

1.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
