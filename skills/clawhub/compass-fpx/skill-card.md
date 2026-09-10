## Description:

Query compass.com from a shell with the fpx CLI to search listings, retrieve property and agent details, inspect price history, and resolve street addresses through one-shot fetches over a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch public Compass real-estate listing, property, agent, address, and price-history data from shell workflows when the Compass MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill pairs fpx with a Compass-scoped browser context and can fetch data using the user's active browser session.

Mitigation: Install and pair only in a browser profile intended for this workflow, keep Chrome site access scoped to compass.com, and review each command before execution.

Risk: Global npm installation and fixed /tmp examples can introduce local environment and file-handling risk.

Mitigation: Pin and review the @fetchproxy/cli version, avoid sudo for npm installs, and replace fixed /tmp paths with a private temporary directory that is cleaned up after use.

Risk: Listing, address, coordinate, photo, and agent data may be sensitive when stored or shared.

Mitigation: Treat fetched real-estate data as potentially sensitive and minimize retention, sharing, and logs.

## Reference(s):

- [Compass fpx request reference](references/requests.md)
- [Compass JSON global extractor](references/extract-global.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, jq filters, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands that fetch Compass pages through a paired browser bridge and extract embedded JSON for downstream processing.]

## Skill Version(s):

0.14.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
