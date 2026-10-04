## Description:

Guides agents to discover Etix events, venues, and performers and retrieve event or venue details through a paired browser using the fpx CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search public Etix listings and retrieve event or venue information from a shell without running the Etix MCP server. It does not support ticket purchases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent browser pairing enables automated requests through a browser session that has passed Etix's bot check.

Mitigation: Confirm the automation is permitted for your use case, restrict extension site access, and revoke pairing or extension access when finished.

Risk: The workflow requires an external CLI and browser extension with access to the browser session.

Mitigation: Review the CLI and extension before installation, and verify the extension package or build it from source.

## Reference(s):

- [Etix consumer endpoints and extraction recipes](references/etix-endpoints.md)
- [Etix dataLayer extraction helper](references/extract-datalayer.mjs)
- [ContextMint Bridge extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [etix-fpx ClawHub release](https://clawhub.ai/chrischall/skills/etix-fpx)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown with shell examples and structured event or venue details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search returns JSON; detail pages require extraction from HTML.]

## Skill Version(s):

1.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
