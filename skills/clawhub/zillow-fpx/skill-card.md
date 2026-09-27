## Description:

Guides agents in retrieving US property listings, property details, market reports, and signed-in saved Zillow data through the fpx browser connection instead of a Zillow MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search US homes, inspect property records and market data, or retrieve their own saved searches and homes without running the Zillow MCP server.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: A connected browser tab can expose private saved searches, favorited homes, addresses, and property data.

Mitigation: Use only with a browser session you trust; avoid shared terminals and CI logs, and review saved-data output before sharing.

## Reference(s):

- [Zillow FPX page recipes](references/pages.md)
- [Zillow FPX ClawHub release](https://clawhub.ai/chrischall/skills/zillow-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples retrieve Zillow page data and may include signed-in saved searches and homes.]

## Skill Version(s):

1.1.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
