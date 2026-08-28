## Description:

Query compass.com (US real-estate portal) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the compass-mcp server: search listings, get property/agent detail, price history, and resolve street addresses through one-shot fetches over a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate data operators use this skill to fetch Compass listing, property, price-history, address-resolution, and agent data from shell workflows using their own browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Compass requests are routed through a browser tab/profile controlled by the user, so fetched data depends on that session and may reflect information visible in that browser context.

Mitigation: Use a Compass tab/profile you control and understand before running the skill.

Risk: Temporary HTML or JSON outputs can contain listing, address, and agent information.

Mitigation: Review /tmp outputs before sharing the machine, logs, or generated files.

Risk: Compass pages can return login or AWS WAF challenge content instead of usable listing data.

Mitigation: Check for the documented login and WAF markers, refresh the Compass tab when blocked, and verify extracted results before relying on them.

## Reference(s):

- [Compass requests for fpx](references/requests.md)
- [extract-global.mjs](references/extract-global.mjs)
- [Compass website](https://www.compass.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands, jq projections, and JSON extraction guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include temporary HTML and JSON files under /tmp that contain listing, address, and agent information.]

## Skill Version(s):

0.12.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
