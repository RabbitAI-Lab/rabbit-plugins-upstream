## Description:

Query compass.com, a US real-estate portal, from a shell with the fpx CLI (@fetchproxy/cli) instead of running compass-mcp, enabling listing search, property and agent detail lookup, price history review, and street-address resolution through one-shot fetches over a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Compass listing, property, agent, and address-resolution data through fetchproxy-backed shell workflows when the Compass MCP server is unavailable or undesired.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a paired fetchproxy browser extension and an open Compass browser tab, so browser profile and session handling affect user privacy.

Mitigation: Use a trusted, pinned local CLI install and a dedicated browser profile or Compass-only tab.

Risk: Fetched page HTML and extracted JSON may contain real-estate search, property, or agent data written to local temporary paths.

Mitigation: Replace sample /tmp paths with a private temporary directory and clean it up after use.

Risk: Compass can return a login or AWS WAF challenge page instead of usable listing data.

Mitigation: Check for the documented login and WAF markers before trusting fetched output, then refresh the Compass tab or repair pairing before retrying.

## Reference(s):

- [Compass request patterns](references/requests.md)
- [Compass global extraction helper](references/extract-global.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, jq filters, and a JavaScript helper script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a paired fetchproxy browser extension, an open compass.com tab, and local handling of fetched HTML or JSON outputs.]

## Skill Version(s):

0.14.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
