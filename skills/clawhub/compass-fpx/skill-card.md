## Description:

Helps agents query Compass real-estate listings, property and agent details, price history, and addresses through a paired browser tab using the fpx CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search US Compass listings and retrieve property, agent, and address information from shell scripts without the Compass MCP server.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The fpx CLI and browser extension send Compass requests through a paired browser tab.

Mitigation: Install and pair the CLI and extension only if you are comfortable granting access to that browser context.

Risk: Temporary files can retain fetched listing, address, or agent data.

Mitigation: Protect or remove temporary output files when the fetched data is sensitive.

## Reference(s):

- [Compass FPX on ClawHub](https://clawhub.ai/chrischall/skills/compass-fpx)
- [Compass request examples](references/requests.md)
- [Compass JSON extraction helper](references/extract-global.mjs)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON data]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listing results depend on the paired browser session; search pages expose a limited first page.]

## Skill Version(s):

1.1.10 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
