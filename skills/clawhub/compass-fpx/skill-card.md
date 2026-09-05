## Description:

Query compass.com from a shell with the fpx CLI instead of running the compass-mcp server, including listing search, property and agent detail, price history, and street-address resolution through one-shot fetches over a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch Compass real-estate search, listing, agent, price-history, and address-resolution data through fetchproxy-backed shell commands when they need scriptable Compass access without installing or running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fetchproxy sends Compass requests through the user's browser session, so the browser extension pairing and site access can affect what data is reachable.

Mitigation: Install only when Compass browser-session routing is intended, keep extension site access scoped to compass.com, and review active pairings.

Risk: Fetched Compass pages and extracted JSON can contain addresses, listing details, and other sensitive real-estate search context in temporary files.

Mitigation: Store temporary HTML and JSON outputs only where appropriate and delete them when the fetched data is no longer needed.

Risk: Login redirects, WAF challenge pages, or stale browser sessions can cause incomplete or misleading fetch results.

Mitigation: Check for login or AWS WAF challenge markers and refresh the Compass tab before trusting extracted results.

## Reference(s):

- [Compass requests for fpx](references/requests.md)
- [extract-global.mjs](references/extract-global.mjs)
- [Compass website](https://www.compass.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with shell commands, JavaScript helper usage, JSON extraction paths, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create temporary HTML or JSON files during Compass fetch and extraction workflows.]

## Skill Version(s):

0.14.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
