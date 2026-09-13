## Description:

Query compass.com from a shell with the fpx CLI to search listings, fetch property and agent details, inspect price history, and resolve street addresses through one-shot requests over a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public Compass real-estate listing, property, agent, price-history, and address-suggestion data from shell workflows when the Compass MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a paired fetchproxy browser bridge to request Compass pages through a signed-in browser tab.

Mitigation: Install only when this browser-bridge posture is acceptable, keep the fpx profile scoped to compass.com, and verify the tab clears Compass WAF challenges before trusting fetched data.

Risk: The setup example installs @fetchproxy/cli globally without a pinned reviewed version.

Mitigation: Pin a reviewed @fetchproxy/cli version or install it locally before operational use.

Risk: Examples use fixed /tmp paths for fetched pages and address-query payloads.

Mitigation: Use a private temporary directory and avoid leaving fetched Compass pages or query payloads in shared filesystem locations.

Risk: Compass search and listing pages can be incomplete, blocked, or stale due to WAF behavior, SSR pagination limits, or relisted properties changing _lid identifiers.

Mitigation: Check the documented login and bot-wall markers, narrow search bands instead of paginating, and prefer stable _pid links for bookmarks or trackers when available.

## Reference(s):

- [Compass requests for fpx](artifact/references/requests.md)
- [extract-global helper](artifact/references/extract-global.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JavaScript helper usage, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on a paired fetchproxy browser bridge and the current Compass page responses.]

## Skill Version(s):

0.14.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
