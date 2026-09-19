## Description:

Query compass.com from a shell with the fpx CLI to search listings, retrieve property and agent details, inspect price history, and resolve street addresses through one-shot fetches over a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agents use this skill to fetch and inspect Compass listing, property, agent, price-history, and address-resolution data from scripts or machines where the Compass MCP server is not installed.

### Deployment Geography for Use:

Global; the skill targets compass.com, described by the artifact as a U.S. real-estate portal.

## Known Risks and Mitigations:

Risk: The skill routes Compass requests through a paired browser tab, which uses the user's active browser context for compass.com.

Mitigation: Install only if this access model is acceptable, keep the paired profile scoped to Compass, and unpair or disable the bridge when it is no longer needed.

Risk: Searches and temporary output files may contain street addresses or listing data.

Mitigation: Avoid storing sensitive searches unnecessarily and delete temporary files such as /tmp/page.html, /tmp/search.json, and /tmp/omni.json after use.

## Reference(s):

- [Compass request guide](references/requests.md)
- [Global extraction helper](references/extract-global.mjs)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/compass-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON and jq examples, and JavaScript helper code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires @fetchproxy/cli, the fetchproxy browser extension, and an open compass.com browser tab.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
