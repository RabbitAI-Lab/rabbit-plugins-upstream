## Description: <br>
Look up Compass real-estate listings, property details, photos, price history, comparable rentals, agent listings, and address resolutions through an MCP integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external real-estate users use this skill to search Compass listings, resolve property addresses, compare listings, inspect photos and price history, and run local mortgage or affordability calculations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill routes Compass property queries through a signed-in browser tab and a third-party MCP package plus browser extension. <br>
Mitigation: Install only in trusted environments and use it only when you are comfortable with those components accessing the active Compass session. <br>
Risk: Address and listing searches can reveal sensitive property interests or location intent. <br>
Mitigation: Avoid entering sensitive or unnecessary personal-property queries and review organizational privacy expectations before use. <br>
Risk: Compass does not publish a public consumer API, so returned listing data depends on currently rendered Compass page state. <br>
Mitigation: Treat outputs as lookup assistance and verify important real-estate details against Compass or other authoritative sources before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass) <br>
- [compass-mcp npm package](https://www.npmjs.com/package/compass-mcp) <br>
- [compass-mcp project link](https://github.com/chrischall/compass-mcp) <br>
- [fetchproxy extension project](https://github.com/chrischall/fetchproxy) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with setup snippets and structured property, listing, photo, price-history, comparison, diagnostic, and calculator results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Network-backed tools are read-only and require compass-mcp, the fetchproxy browser extension, and an active signed-in Compass browser tab; local mortgage and affordability calculations do not require sign-in.] <br>

## Skill Version(s): <br>
0.12.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
