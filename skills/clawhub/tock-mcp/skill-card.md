## Description: <br>
Discover restaurants on Tock through MCP, including metros, venue search, venue details, bookable experiences, prices, party sizes, and availability dates and times. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an agent to the tock-mcp server for read-only Tock restaurant discovery, availability lookup, and reservation or profile review through their signed-in browser session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The MCP server and fetchproxy extension can read Tock pages from the user's browser session, including profile and reservation data when those tools are invoked. <br>
Mitigation: Install and run it only with a Tock session the user is comfortable exposing to the MCP workflow, and review the external npm package and browser extension before deployment. <br>
Risk: Booking and payment remain outside the skill, but returned availability or reservation information may influence user decisions. <br>
Mitigation: Treat tool output as read-only discovery data and complete booking, cancellation, and payment directly on Tock's website. <br>


## Reference(s): <br>
- [tock-mcp npm package](https://www.npmjs.com/package/tock-mcp) <br>
- [tock-mcp source repository](https://github.com/chrischall/tock-mcp) <br>
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline JSON and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides an agent to use read-only MCP tools and leaves booking, cancellation, and payment actions to Tock's website.] <br>

## Skill Version(s): <br>
0.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
