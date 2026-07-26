## Description: <br>
Automate Amplitude analytics tasks through Rube MCP, including event sending, user activity retrieval, cohort management, and user identification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sohamganatra](https://clawhub.ai/user/sohamganatra) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and analytics operators use this skill to guide an agent through Amplitude workflows over a connected Rube MCP account. It helps send events, find users, inspect activity, update user properties, and manage cohorts while checking current tool schemas first. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A connected Amplitude account can expose user activity and analytics data. <br>
Mitigation: Confirm the workspace and target user identifiers before reading activity, minimize raw user data exposure, and revoke the Rube/Amplitude connection when it is no longer needed. <br>
Risk: Event, identify, and cohort workflows can change analytics data or cohort membership. <br>
Mitigation: Review event payloads, user property operations, and cohort IDs before execution; check asynchronous cohort status after updates. <br>
Risk: Tool schemas and rate limits may change over time. <br>
Mitigation: Search the Rube MCP tools first for current schemas, batch event calls where appropriate, and chunk large cohort updates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sohamganatra/skills/amplitude-automation) <br>
- [Rube MCP endpoint](https://rube.app/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with tool sequences, parameter notes, JSON examples, and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill produces agent-facing workflow guidance and does not itself execute Amplitude changes.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
