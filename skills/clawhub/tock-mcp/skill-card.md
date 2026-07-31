## Description: <br>
Discover restaurants on Tock (exploretock.com) via MCP, including cities, metro search, venue details, bookable experiences, prices, party sizes, and open dates or times. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to Tock restaurant discovery and availability workflows through the tock-mcp MCP server. It can retrieve restaurant, availability, reservation, and profile information while leaving booking and payment actions on exploretock.com. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup routes Tock requests through a signed-in browser session, and account tools can expose profile or reservation information to the MCP client. <br>
Mitigation: Install only trusted copies of the npm package and fetchproxy extension, and use the skill only with a Tock session whose profile and reservation details may be shared with the connected MCP client. <br>
Risk: Availability and profile data depend on exploretock.com pages, browser session state, and any Cloudflare challenge presented to the user. <br>
Mitigation: Resolve browser sign-in or challenge prompts in the Tock tab, and verify availability, pricing, and reservation terms directly on exploretock.com before making plans. <br>
Risk: The skill is read-only and does not complete booking, cancellation, or payment actions. <br>
Mitigation: Complete prepaid reservations or account changes directly on Tock after confirming the details shown by the agent. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-mcp) <br>
- [tock-mcp npm package](https://www.npmjs.com/package/tock-mcp) <br>
- [tock-mcp source link from artifact](https://github.com/chrischall/tock-mcp) <br>
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires tock-mcp and the fetchproxy browser extension; Tock account tools require a signed-in exploretock.com browser tab.] <br>

## Skill Version(s): <br>
0.2.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
