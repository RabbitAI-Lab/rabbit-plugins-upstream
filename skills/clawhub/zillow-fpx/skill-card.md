## Description: <br>
Query zillow.com from a shell with the fpx CLI to search listings, retrieve property records, history, photos, market reports, and signed-in saved searches or homes through a browser tab. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to fetch Zillow listing, property, history, photo, market report, saved search, and saved home data with one-shot shell commands. It is useful when Zillow data is needed without running a Zillow MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands may access private saved searches or favorited homes from a signed-in Zillow tab. <br>
Mitigation: Treat saved-search and saved-home results as private account data, avoid unnecessary logging or persistence, and remove or re-pair the fpx profile when access should no longer persist. <br>
Risk: Fetches depend on a user-approved browser bridge and an active Zillow tab, so signed-out redirects, bot-wall pages, or bridge failures may appear instead of usable Zillow data. <br>
Mitigation: Check fetched HTML for login or bot-wall markers, use the documented fpx health check, and confirm the browser extension, site access, pairing, and zillow.com tab state before relying on results. <br>


## Reference(s): <br>
- [Zillow pages for fpx](artifact/references/pages.md) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zillow-fpx) <br>
- [Publisher profile](https://clawhub.ai/user/chrischall) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline shell, Python, jq, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires fpx, the fetchproxy browser extension, and an active zillow.com browser tab for live data fetching.] <br>

## Skill Version(s): <br>
0.11.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
