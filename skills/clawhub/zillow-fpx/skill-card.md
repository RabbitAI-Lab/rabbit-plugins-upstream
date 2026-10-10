## Description:

Guides agents in retrieving US Zillow listings, property details, market reports, and signed-in saved data through a browser-backed shell CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search US property listings and inspect Zillow property, pricing, tax, photo, and market data without running the Zillow MCP server. Signed-in users can also retrieve their saved searches and homes.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The CLI and browser extension can access Zillow pages through the user's browser session.

Mitigation: Install and pair them only if you are comfortable granting that access; review the extension before use.

Risk: Saved searches, saved homes, and exact-address queries can expose account or location data to local scripts and command output.

Mitigation: Run those examples only when needed, and avoid sharing captured outputs or temporary files containing sensitive data.

## Reference(s):

- [Zillow pages for fpx](references/pages.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/zillow-fpx)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Retrieved results may contain property addresses or signed-in saved-listing data.]

## Skill Version(s):

1.2.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
