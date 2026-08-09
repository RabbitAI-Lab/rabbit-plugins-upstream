## Description:

Query Compass real-estate data from a shell with the fpx CLI to search listings, inspect property and agent details, read price history, and resolve street addresses through one-shot fetches over a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate data analysts use this skill to generate Compass fetch commands and parsing steps for listing search, property detail, agent listings, price history, and address resolution without running a Compass MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Compass requests are routed through a paired browser extension using the user's open Compass browser session.

Mitigation: Use a dedicated browser profile when appropriate, approve pairing intentionally, and remove the fpx pairing when the bridge is no longer needed.

Risk: Fetches can return a login page or AWS WAF challenge instead of usable Compass data.

Mitigation: Check for login or WAF markers before trusting fetched output, refresh the Compass tab when challenged, and retry only after the tab has a valid session.

Risk: Compass search pages expose only the first server-rendered result page and may omit broader market coverage.

Mitigation: Narrow searches by price, bed count, or property type and verify important results against the live Compass page.

## Reference(s):

- [Compass requests for fpx](references/requests.md)
- [extract-global.mjs](references/extract-global.mjs)
- [Compass website](https://www.compass.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass-fpx)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with shell commands, JavaScript helper usage, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs assume a paired fetchproxy browser extension, an open Compass tab, and local tools such as fpx, Node.js, and jq.]

## Skill Version(s):

0.12.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
