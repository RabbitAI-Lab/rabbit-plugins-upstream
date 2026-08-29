## Description:

Read Workday HR data through a read-only MCP server that uses the user's signed-in Workday browser session and fetchproxy extension.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to let an agent retrieve Workday org chart, worker profile, compensation, benefits, performance, task, and data-card information available to the signed-in account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive Workday HR data available to the signed-in account, including employee, compensation, benefits, and performance information.

Mitigation: Use it only after checking employer policy, and manually confirm sensitive HR-data requests before allowing the agent to proceed.

Risk: The skill relies on a live browser session and fetchproxy pairing, so unintended trust or stale pairing could broaden access.

Mitigation: Approve pairing only for this MCP and expected Workday domains, and revoke fetchproxy trust when the skill is no longer in use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-mcp)
- [workday-mcp npm package](https://www.npmjs.com/package/workday-mcp)
- [workday-mcp source](https://github.com/chrischall/workday-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown instructions with inline JSON configuration, shell commands, and MCP tool outputs as structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Workday data retrieval through the user's live authenticated browser session.]

## Skill Version(s):

0.4.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
