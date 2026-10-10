## Description:

Helps agents query Compass real-estate listings, property details, price histories, and agent profiles through the fpx CLI and a paired browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search US real-estate listings, inspect property and agent details, check price history, and resolve addresses from Compass without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a global CLI and browser extension adds software with access to browser-mediated requests.

Mitigation: Install only if comfortable with both components; use a dedicated browser profile or Compass session and limit extension site access to compass.com.

Risk: The browser bridge pairing persists and can expose browsing-session data to later requests.

Mitigation: Remove the pairing when no longer needed and keep the browser session limited to the intended Compass use.

## Reference(s):

- [Compass fpx request recipes](references/requests.md)
- [Compass fpx release](https://clawhub.ai/chrischall/skills/compass-fpx)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Text or JSON with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listing results depend on the available Compass pages and the paired browser session.]

## Skill Version(s):

1.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
