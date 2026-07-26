## Description: <br>
Look up Redfin real-estate listings, property details, market reports, mortgage estimates, and saved homes or searches through an MCP server connected to the user's active Redfin browser session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask an agent for Redfin listing searches, property details, market reports, mortgage calculations, and account-linked saved Redfin homes or searches. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Saved Redfin homes and searches can appear in agent responses when account-linked tools use the active signed-in browser session. <br>
Mitigation: Install only for users and agents permitted to access that Redfin account, and review requests before invoking saved-data tools. <br>
Risk: The skill depends on Redfin web-app endpoints and a browser-mediated session, so access may fail when sign-in state, WAF challenges, or site behavior changes. <br>
Mitigation: Keep the browser session signed in, resolve browser challenges manually, and treat failures or changed output as expected operational conditions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/redfin-mcp) <br>
- [redfin-mcp npm package](https://www.npmjs.com/package/redfin-mcp) <br>
- [redfin-mcp source repository](https://github.com/chrischall/redfin-mcp) <br>
- [fetchproxy source repository](https://github.com/chrischall/fetchproxy) <br>


## Skill Output: <br>
**Output Type(s):** [text, configuration, shell commands] <br>
**Output Format:** [Markdown or structured text from MCP tool results, with JSON and shell snippets for setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Redfin data access; saved-home and saved-search tools require an active signed-in Redfin browser session.] <br>

## Skill Version(s): <br>
0.9.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
