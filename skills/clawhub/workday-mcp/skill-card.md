## Description: <br>
Read-only MCP skill for retrieving Workday HR tasks, pay, benefits, and compensation data through the user's signed-in browser session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and authorized Workday users use this skill to inspect their own Workday tasks and HR data, including pay, benefits, compensation, and related task details, from an agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose private HR, pay, benefits, and compensation data available in the user's signed-in Workday browser session. <br>
Mitigation: Install only when acceptable under employer policy, keep prompts explicit when requesting Workday data, and disable or remove the MCP and extension pairing when it is no longer needed. <br>
Risk: The browser extension bridge depends on the user's live Workday session and approved local pairing. <br>
Mitigation: Use the health check to confirm the bridge and session state, approve pairing only for the intended MCP server, and re-authenticate or disconnect when the session is no longer intended for agent access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-mcp) <br>
- [workday-mcp npm package](https://www.npmjs.com/package/workday-mcp) <br>
- [fetchproxy extension setup](https://github.com/chrischall/fetchproxy) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, configuration, guidance] <br>
**Output Format:** [Structured JSON from MCP tools with Markdown setup and usage guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Workday access; requires workday-mcp, the fetchproxy browser extension, tenant configuration, and an active signed-in Workday browser session.] <br>

## Skill Version(s): <br>
0.2.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
