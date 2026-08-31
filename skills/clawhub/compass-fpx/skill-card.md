## Description:

Query compass.com real-estate data from a shell with the fpx CLI, including listing search, property and agent detail, price history, and address resolution through one-shot fetches over a paired browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Compass listing, property, agent, price-history, and address-resolution data from shell workflows when the Compass MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Compass requests are routed through the browser profile and Compass tab paired with fetchproxy.

Mitigation: Use a browser account and session intended for these queries, and remove or change the pairing when that session should no longer be used.

Risk: Compass pages can return login or AWS WAF challenge responses instead of usable listing data.

Mitigation: Check for login and WAF challenge markers before trusting a fetch, then refresh the compass.com tab or re-pair fetchproxy when needed.

## Reference(s):

- [Compass request recipes](references/requests.md)
- [Compass global extractor](references/extract-global.mjs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON extraction examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance assumes a paired fetchproxy browser extension, an open compass.com tab, and jq or Node-based extraction for structured results.]

## Skill Version(s):

0.13.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
