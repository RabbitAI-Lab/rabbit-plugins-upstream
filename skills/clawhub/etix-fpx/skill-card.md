## Description:

Query etix.com event-discovery data from a shell with the fpx CLI, including event, venue, performer, geolocation, and detail lookups through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public Etix discovery data from shell workflows when the Etix MCP server is unavailable, unnecessary, or not installed. It is intended for anonymous discovery reads, not ticket purchasing or seller API access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on installing fpx and npm packages.

Mitigation: Review the npm install commands and pin package versions where your environment requires deterministic dependencies.

Risk: The persistent Etix-scoped browser bridge can reuse an approved browser pairing.

Mitigation: Use a browser profile without sensitive Etix state and revoke the Etix fpx pairing when finished.

Risk: Etix HTML responses can still be DataDome interstitials even when a fetch command exits successfully.

Mitigation: Check responses for the documented DataDome markers before parsing or trusting returned HTML.

## Reference(s):

- [Etix consumer endpoints for fpx](references/etix-endpoints.md)
- [extract-datalayer.mjs](references/extract-datalayer.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix-fpx)
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command recipes and extraction guidance; retrieved Etix data may be JSON or HTML that requires local parsing.]

## Skill Version(s):

0.6.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
