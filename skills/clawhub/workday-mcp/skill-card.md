## Description: <br>
Read-only Workday MCP helper that lets an agent fetch tasks, pay, benefits, and compensation data through the user's signed-in browser session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and their agents use this skill to read Workday tasks and HR data, including pay, benefits, and compensation, from the user's active signed-in Workday browser session. It is intended for read-only retrieval and navigation of information visible to that user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose sensitive Workday HR, pay, benefits, and compensation data to the agent. <br>
Mitigation: Install only when comfortable sharing Workday data visible in the signed-in browser, keep the browser extension limited to Workday where possible, and ask the agent to confirm before fetching especially sensitive pages. <br>
Risk: Use may be constrained by an employer's acceptable-use policy for Workday access. <br>
Mitigation: Review the employer's acceptable-use policy before use and keep activity limited to read-only retrieval of the user's own data. <br>


## Reference(s): <br>
- [workday-mcp npm package](https://www.npmjs.com/package/workday-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON configuration and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The MCP tools return structured JSON describing Workday apps, tasks, data-card fields, references, related tasks, export links, and health-check status.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
