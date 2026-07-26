## Description: <br>
Looks up Homes.com real-estate listings, property details, price and tax history, market reports, saved homes, saved searches, and photo galleries through an MCP server that uses a signed-in browser session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, home buyers, real-estate researchers, and developers use this skill to query Homes.com listing, property, history, photo, saved-account, and market data through an MCP server. The skill also provides local mortgage, affordability, and rent-versus-buy calculators. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a signed-in Homes.com browser tab and may access private saved homes or saved searches. <br>
Mitigation: Install only if you are comfortable sharing account-linked housing preference data with the agent, and avoid saved-home or saved-search tools unless you explicitly intend that access. <br>
Risk: The skill depends on a browser extension and a live Homes.com session, so browser challenges, authentication state, or extension availability can affect results. <br>
Mitigation: Keep the fetchproxy extension connected, review session diagnostics, and verify important real-estate outputs against Homes.com before acting on them. <br>


## Reference(s): <br>
- [Homes MCP ClawHub release](https://clawhub.ai/chrischall/skills/homes-mcp) <br>
- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp) <br>
- [homes-mcp source reference](https://github.com/chrischall/homes-mcp) <br>
- [fetchproxy setup reference](https://github.com/chrischall/fetchproxy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON configuration snippets, shell commands, and structured MCP tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Homes.com lookups may include listing data, property records, photos, price/tax history, market summaries, saved homes/searches, diagnostics, and local calculator results.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
