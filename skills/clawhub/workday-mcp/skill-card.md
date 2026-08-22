## Description:

Read Workday HR data through a user's signed-in Workday browser session via MCP, including org charts, worker profiles, pay, benefits, compensation, performance, and task or data cards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, managers, and developers use this skill to let an agent retrieve read-only Workday people, organization, compensation, benefits, performance, and task data from the user's own authenticated Workday session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read highly sensitive HR data, including compensation, benefits, performance, and other employee data, through a live signed-in browser session.

Mitigation: Install only when this access is deliberate, confirm before using sensitive HR data, and check the employer's acceptable-use policy.

Risk: The skill depends on a local MCP package and fetchproxy browser extension that bridge agent requests into an authenticated Workday session.

Mitigation: Prefer project-scoped MCP configuration and verify the npm package and fetchproxy extension source before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-mcp)
- [npm package](https://www.npmjs.com/package/workday-mcp)
- [workday-mcp source](https://github.com/chrischall/workday-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce structured JSON returned by MCP tools when the backing Workday MCP server is available.]

## Skill Version(s):

0.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
