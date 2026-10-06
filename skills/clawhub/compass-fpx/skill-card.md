## Description:

Helps agents query Compass US real-estate listings, property and agent details, price history, and addresses through the fpx CLI and a paired browser tab without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search US Compass listings, inspect property and agent information, and resolve addresses from shell-driven workflows without the Compass MCP server.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Browser-bridge pairing persists and relies on an external extension and CLI package.

Mitigation: Review the ContextMint Bridge extension and fpx package before installation, and revoke pairing when no longer needed.

## Reference(s):

- [ClawHub compass-fpx release](https://clawhub.ai/chrischall/skills/compass-fpx)
- [Compass request examples](references/requests.md)
- [Compass JSON extraction utility](references/extract-global.mjs)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell commands and JSON extraction examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listing search pages expose a limited first page; further coverage requires narrower searches.]

## Skill Version(s):

1.1.7 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
