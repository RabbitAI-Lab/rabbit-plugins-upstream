## Description: <br>
Look up Compass real-estate listings, property details, photos, price history, address resolutions, comparisons, and mortgage calculations through a local MCP setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to connect to Compass lookup tools for read-only real-estate research, listing comparison, address resolution, photo retrieval, price history review, and local housing-payment calculations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Network-backed tools use the user's signed-in Compass browser session. <br>
Mitigation: Install and enable the skill only when you intend the agent to query Compass, and review Compass-related prompts before allowing tool use. <br>
Risk: The MCP package and fetchproxy browser extension are external dependencies. <br>
Mitigation: Review and trust those dependencies separately before deployment. <br>
Risk: Compass access depends on a signed-in tab and may fail when authentication, WAF challenges, or unsupported saved-home and saved-search flows are encountered. <br>
Mitigation: Keep the Compass browser session active, solve browser challenges in the tab when needed, and treat unsupported saved-home or saved-search requests as unavailable rather than relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass-mcp) <br>
- [compass-mcp npm package](https://www.npmjs.com/package/compass-mcp) <br>
- [compass-mcp source](https://github.com/chrischall/compass-mcp) <br>
- [fetchproxy source](https://github.com/chrischall/fetchproxy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON and shell command snippets; MCP tool responses return real-estate lookup text and structured data.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires compass-mcp, the fetchproxy extension, and a signed-in Compass browser session for network-backed tools.] <br>

## Skill Version(s): <br>
0.11.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
