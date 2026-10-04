## Description:

Helps agents query Compass real-estate listings, property and agent details, price history, and addresses from a shell through a browser-backed CLI instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up US real-estate listings, property and agent details, price history, and street addresses on Compass from shell-based workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a third-party CLI and browser extension with persistent pairing.

Mitigation: Review @fetchproxy/cli and ContextMint Bridge before installation and approve pairing only for intended use.

Risk: Broad browser-extension site access could expose browsing activity outside the intended Compass lookups.

Mitigation: Limit the extension's site access to compass.com and use the skill only for intended Compass data lookups.

## Reference(s):

- [Compass FPX release on ClawHub](https://clawhub.ai/chrischall/skills/compass-fpx)
- [Compass request examples](references/requests.md)
- [Compass page-data extraction helper](references/extract-global.mjs)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and JSON field examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compass listing and address results depend on the connected browser tab and available page data.]

## Skill Version(s):

1.1.6 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
