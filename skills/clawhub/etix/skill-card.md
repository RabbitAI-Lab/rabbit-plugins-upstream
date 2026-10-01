## Description:

Searches Etix events, venues, and performers and retrieves event and venue details through a browser-connected MCP integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People looking for live events use this skill to find Etix listings and get event dates, venue details, and available price information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: This unofficial integration uses an Etix browser session and a separate extension.

Mitigation: Review the MCP package and extension source or release checksums before installation, and approve browser pairing only when expected.

Risk: Etix website changes or access restrictions may interrupt event searches.

Mitigation: Use the integration only for event discovery consistent with Etix's terms and verify important event details on Etix.

## Reference(s):

- [Etix skill on ClawHub](https://clawhub.ai/chrischall/skills/etix)
- [etix-mcp package](https://www.npmjs.com/package/etix-mcp)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with event and venue details and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event results may include dates, venues, organizers, and ticket prices.]

## Skill Version(s):

1.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
