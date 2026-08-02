## Description: <br>
Look up real-estate listings, property details, Zestimates, saved searches/homes, and market reports on Zillow via MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query Zillow property listings, property records, Zestimates, market reports, saved searches, and saved homes through an MCP server backed by the user's browser session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an unofficial Zillow automation path through private Zillow web endpoints and a signed-in browser session. <br>
Mitigation: Install only after reviewing the fetchproxy extension permissions, and avoid bulk or commercial use that could conflict with Zillow's terms. <br>
Risk: Saved homes and saved searches can expose personal real-estate activity. <br>
Mitigation: Treat saved Zillow data as personal data and run the skill only in contexts where that browser session is appropriate. <br>
Risk: Zillow may present captcha or authentication interstitials that block requests. <br>
Mitigation: Resolve authentication or captcha prompts in the active Zillow browser tab before retrying tool calls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zillow) <br>
- [zillow-mcp npm package](https://www.npmjs.com/package/zillow-mcp) <br>
- [zillow-mcp source](https://github.com/chrischall/zillow-mcp) <br>
- [fetchproxy source](https://github.com/chrischall/fetchproxy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline JSON and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Zillow query results may include personal saved-home or saved-search data when the user is signed in.] <br>

## Skill Version(s): <br>
0.11.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
