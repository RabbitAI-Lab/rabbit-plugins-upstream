## Description:

Query etix.com event discovery data from a shell with the @fetchproxy/cli fpx CLI to search events, venues, and performers and retrieve event or venue details through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate fpx setup commands, Etix lookup calls, and parsing recipes for public event, venue, performer, and geolocation discovery without running etix-mcp.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a browser extension bridge with persistent pairing for etix.com, and lookup commands may send search terms or city/postal-code values to Etix.

Mitigation: Use a trusted paired browser profile, review commands before execution, and avoid sensitive search terms or locations.

Risk: Dependency and temporary-file hygiene issues can arise from global npm installs, unpinned packages, elevated installs, or fixed /tmp paths.

Mitigation: Prefer pinned npm versions, avoid elevated install privileges, and use private temporary directories for fetched HTML and JSON files.

Risk: An HTML fetch can exit successfully while returning a DataDome interstitial instead of event or venue content.

Mitigation: Check fetched HTML for captcha-delivery or the documented ad-blocker message before parsing it as Etix content.

Risk: Buying tickets is a financial action outside the scope of the skill.

Mitigation: Limit use to anonymous discovery reads and do not use the generated commands for ticket purchases.

## Reference(s):

- [Etix consumer endpoints for fpx](references/etix-endpoints.md)
- [extract-datalayer.mjs](references/extract-datalayer.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON and jq examples, and JavaScript helper code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one-shot fpx command patterns and parsing guidance for Etix discovery data; it does not purchase tickets.]

## Skill Version(s):

0.6.1 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
