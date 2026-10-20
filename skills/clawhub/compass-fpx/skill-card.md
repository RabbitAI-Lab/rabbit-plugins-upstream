## Description:

Helps agents query Compass property listings, listing and agent details, price history, and address suggestions through a paired browser tab using the fpx CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve US real-estate listing, property, agent, and address information from Compass without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bridge extension and fpx CLI can make requests through an active browser session.

Mitigation: Review the extension and CLI package provenance before installation, and approve pairing only for the intended Compass tab.

Risk: Address suggestions may return an unrelated property match.

Mitigation: Confirm street, city, and state against the suggested address before relying on its listing ID.

## Reference(s):

- [Compass FPX on ClawHub](https://clawhub.ai/chrischall/skills/compass-fpx)
- [Compass request examples](artifact/references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, JSON]

**Output Format:** [Markdown instructions with shell commands and JSON extraction examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compass US property data; requires a paired browser tab and bridge extension. Search pages show only the first approximately 41 listings.]

## Skill Version(s):

1.1.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
