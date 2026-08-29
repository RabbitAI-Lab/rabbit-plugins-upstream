## Description:

Query compass.com from a shell with the fpx CLI to search listings, fetch property and agent details, inspect price history, and resolve street addresses through one-shot requests over a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public Compass real-estate listing, property, price-history, address-suggestion, and agent-listing data from shell workflows when the Compass MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests run through a signed-in browser-session bridge, so fetched HTML or JSON may reflect the user's active Compass session context.

Mitigation: Install only when fpx, the fetchproxy extension, and receiving local scripts are trusted; use a dedicated Compass browser profile for stronger isolation.

Risk: Fetched Compass HTML or extracted JSON may be left in predictable temporary files.

Mitigation: Avoid predictable /tmp paths or remove temporary files when fetched data could reveal session-specific context.

Risk: Compass can return login pages or AWS WAF challenge pages instead of usable listing data.

Mitigation: Check for the documented login and WAF markers before trusting parsed output, then refresh the Compass tab or re-pair fpx when needed.

## Reference(s):

- [Compass requests for fpx](references/requests.md)
- [extract-global.mjs](references/extract-global.mjs)
- [Compass](https://www.compass.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, jq projections, endpoint paths, and helper JavaScript usage.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include commands that write fetched Compass HTML or JSON to local files for later parsing.]

## Skill Version(s):

0.12.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
