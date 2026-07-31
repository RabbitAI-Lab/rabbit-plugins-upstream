## Description: <br>
Query compass.com from a shell with the fpx CLI to search listings, get property and agent details, inspect price history, and resolve street addresses through one-shot fetches over a signed-in browser tab. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and analysts use this skill to query Compass listing, property, agent, price history, and address data from shell scripts via fpx when they do not want to run the Compass MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Requests are made through the Compass browser tab and session selected by the user. <br>
Mitigation: Use a browser profile or session intended for this purpose and avoid pairing through a session that should not be used for Compass requests. <br>
Risk: Fetchproxy pairing persists after the initial approval. <br>
Mitigation: Remove or disable the pairing when the workflow is no longer needed. <br>
Risk: Compass search pages have coverage and reliability limits, including WAF behavior and a first-page server-rendering ceiling. <br>
Mitigation: Check for bot-wall responses before trusting fetched pages, prefer the structured address typeahead for address resolution, and narrow searches with price or bed filters instead of relying on pagination. <br>


## Reference(s): <br>
- [Compass requests for fpx](references/requests.md) <br>
- [extract-global.mjs](references/extract-global.mjs) <br>
- [Compass](https://www.compass.com) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass-fpx) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, jq projections, and JavaScript helper usage.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the fetchproxy CLI and browser extension paired to a compass.com tab; requests use the user's selected browser session.] <br>

## Skill Version(s): <br>
0.12.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
