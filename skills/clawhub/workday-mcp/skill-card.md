## Description:

Read Workday HR data such as org charts, worker profiles, pay, benefits, compensation, performance, and task or data cards through MCP using the user's signed-in Workday browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and employees use this skill to let an agent read Workday information available in their own signed-in session, including org charts, worker profiles, tasks, pay, benefits, compensation, and performance data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read sensitive Workday HR data available in the user's signed-in browser session, including compensation, benefits, performance, pay history, inbox items, and worker profile data.

Mitigation: Install only when this access is acceptable for the intended user and organization, and require explicit confirmation before sensitive reads.

Risk: The setup depends on third-party package and fetchproxy installation steps that may change over time.

Mitigation: Prefer a reviewed pinned workday-mcp package version and pinned fetchproxy commit before deployment.

Risk: Raw fetch and GraphQL tools can expose broad Workday data beyond the typed helper tools.

Mitigation: Use typed tools first, avoid broad raw reads unless needed, and review requested queries before execution.

## Reference(s):

- [workday-mcp ClawHub page](https://clawhub.ai/chrischall/skills/workday-mcp)
- [workday-mcp npm package](https://www.npmjs.com/package/workday-mcp)
- [fetchproxy extension source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and structured JSON data returned by MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Workday MCP access through the user's signed-in browser session; compact and full response views are available on selected deep-read tools.]

## Skill Version(s):

0.6.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
