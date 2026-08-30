## Description:

workday-mcp lets an agent read Workday HR data, including org charts, worker profiles, pay, benefits, compensation, performance, and task or data cards, through the user's signed-in Workday browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees or authorized workplace users use this skill to ask an agent to retrieve Workday org, profile, compensation, benefits, performance, and task data available through their own authenticated browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive Workday HR data through the user's signed-in browser session.

Mitigation: Install and use it only when employer policy permits automated Workday access, and request sensitive employee records only when authorized and intentional.

Risk: The release security summary says the documentation understates the privacy boundary.

Mitigation: Review the security guidance before installation and treat all retrieved Workday data as sensitive workplace information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-mcp)
- [workday-mcp npm package](https://www.npmjs.com/package/workday-mcp)
- [fetchproxy setup dependency](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Workday data retrieval through the user's authenticated browser session; may return structured JSON from MCP tool calls.]

## Skill Version(s):

0.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
