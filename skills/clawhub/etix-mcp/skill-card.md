## Description: <br>
Search Etix events, venues, and performers and pull event and venue details through an MCP server that uses an active Etix browser tab. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to search public Etix event data, retrieve event details, inspect venues, resolve locations, and check the browser-session bridge used by the MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill routes Etix requests through the user's active browser session and fetchproxy extension. <br>
Mitigation: Install and invoke it only when you intend your active Etix tab to participate, and review the extension and npm package source before use. <br>
Risk: Etix does not provide a public consumer API, so site behavior and terms may change. <br>
Mitigation: Use the skill at your discretion, keep usage consistent with Etix terms, and run the healthcheck when tool calls fail. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix-mcp) <br>
- [etix-mcp npm package](https://www.npmjs.com/package/etix-mcp) <br>
- [etix-mcp source](https://github.com/chrischall/etix-mcp) <br>
- [fetchproxy source](https://github.com/chrischall/fetchproxy) <br>
- [Etix ticket site](https://www.etix.com/ticket/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Shell commands, MCP tool calls, Text] <br>
**Output Format:** [Markdown with JSON and bash snippets, plus MCP tool-call guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires etix-mcp, the fetchproxy browser extension, and an active etix.com tab for tool calls.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
