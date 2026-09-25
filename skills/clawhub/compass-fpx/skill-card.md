## Description:

Query compass.com from a shell with the fpx CLI to search listings, get property and agent details, read price history, and resolve street addresses through one-shot fetches over a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch Compass real-estate search, listing, price-history, address-resolution, and agent-listing data from shell workflows without running the Compass MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: fpx requests use the browser session context associated with a paired Compass tab.

Mitigation: Limit the fpx profile to compass.com, query only data you intend to access, and remove the pairing when the skill is no longer needed.

Risk: Compass may return a login page or AWS WAF challenge instead of the expected data page.

Mitigation: Check for login redirects and AWS WAF markers before trusting fetched HTML, then refresh the Compass tab or re-pair fetchproxy if needed.

Risk: Compass SSR search results expose only the first rendered result set, so broad searches can be incomplete.

Mitigation: Narrow searches with price, bed, and home-type bands and re-run each band instead of relying on pagination.

## Reference(s):

- [Compass request recipes](references/requests.md)
- [Compass global extraction helper](references/extract-global.mjs)
- [Compass website](https://www.compass.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, JSON extraction examples, and jq projections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command recipes and parsing guidance for Compass HTML and JSON responses; the skill itself does not expose a long-running service.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
