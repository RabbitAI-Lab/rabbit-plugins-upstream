## Description:

Read Workday HR data, including org charts, worker profiles, pay, benefits, compensation, performance, tasks, and data cards, through the user's own signed-in Workday session via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, managers, and their authorized agents use this skill to read Workday HR information visible in their own signed-in browser session, including org charts, worker profiles, pay, benefits, performance, tasks, and data cards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read highly sensitive HR data visible in a live signed-in Workday browser session.

Mitigation: Install only after reviewing employer policy, keep the browser extension paired only when needed, and require explicit confirmation before fetching compensation, benefits, performance, or another worker's records.

Risk: The skill has broad invocation scope around Workday people, pay, benefits, performance, and team data.

Mitigation: Limit prompts to necessary Workday tasks and review returned data before using or sharing it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-mcp)
- [workday-mcp npm package](https://www.npmjs.com/package/workday-mcp)
- [fetchproxy extension source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses may include structured Workday data read from the user's signed-in browser session.]

## Skill Version(s):

0.6.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
