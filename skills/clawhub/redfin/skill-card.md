## Description: <br>
Look up real-estate listings, property details, market reports, and your saved homes/searches on Redfin via MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query Redfin listings, property records, market reports, mortgage calculations, and their saved Redfin homes or searches through an MCP-enabled agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill routes Redfin requests through a logged-in browser session and can expose saved homes or saved searches to the agent context. <br>
Mitigation: Install only when that account access is acceptable, keep the browser session scoped to the intended user, and avoid sharing agent transcripts that contain saved Redfin activity. <br>
Risk: The required fetchproxy browser extension has broad browser access and incomplete disclosure in the skill text. <br>
Mitigation: Review the npm package and extension source before use, limit Chrome site access to Redfin where possible, and remove or disable the extension when it is not needed. <br>
Risk: The skill uses Redfin private endpoints through the user's browser session. <br>
Mitigation: Use at personal scale, avoid bulk or commercial scraping behavior, and stop use if Redfin access controls or terms prohibit the activity. <br>


## Reference(s): <br>
- [Redfin MCP npm package](https://www.npmjs.com/package/redfin-mcp) <br>
- [redfin-mcp source repository](https://github.com/chrischall/redfin-mcp) <br>
- [fetchproxy browser extension source](https://github.com/chrischall/fetchproxy) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JSON configuration snippets, shell commands, and MCP tool outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Redfin query results may include listing details, market metrics, mortgage calculations, and signed-in saved homes or searches.] <br>

## Skill Version(s): <br>
0.10.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
