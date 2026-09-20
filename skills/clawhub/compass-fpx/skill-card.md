## Description:

Query compass.com from a shell with the fpx CLI to search listings, retrieve property and agent details, inspect price history, and resolve street addresses through one-shot fetches over a paired browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate data workflows use this skill to fetch Compass search, listing, agent, price-history, and address-resolution data from a shell when the Compass MCP server is not installed or not desired.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Compass requests through a paired browser tab, which can reuse an authenticated browser context.

Mitigation: Use a dedicated browser profile or tab with site access limited to compass.com, and review requests before using the helper on sensitive authenticated sessions.

Risk: Compass pages can redirect to login or return an AWS WAF challenge instead of listing data.

Mitigation: Check for login and WAF challenge markers before trusting fetched output, and refresh the compass.com tab or re-pair fpx when bridge or bot-wall errors occur.

## Reference(s):

- [Compass request recipes](references/requests.md)
- [Compass JSON global extractor](references/extract-global.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JavaScript snippets, and JSON/jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a paired fetchproxy browser extension profile for compass.com and user review of requests on sensitive sessions.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
