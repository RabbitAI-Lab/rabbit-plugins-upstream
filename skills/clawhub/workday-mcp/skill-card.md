## Description:

Read-only MCP helper that lets an agent retrieve Workday org charts, worker profiles, compensation, benefits, performance, tasks, and data cards through the user's signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized Workday users use this skill to let an agent read HR information that is visible in their own signed-in Workday session. It supports questions about org structure, worker profiles, pay, benefits, performance, apps, tasks, and Workday data cards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server and paired browser extension can read sensitive Workday HR data visible in the user's signed-in session.

Mitigation: Use only with explicit authorization, confirm employer acceptable-use rules, and avoid accessing compensation, benefits, performance, or worker data for anyone unless clearly permitted.

Risk: The release relies on mutable third-party npm package code and a separate fetchproxy browser extension source.

Mitigation: Pin and verify the npm package and fetchproxy source before use, and prefer project-local MCP configuration over global configuration.

Risk: A persistent browser bridge can continue exposing Workday session data while paired and active.

Mitigation: Install only when this access posture is acceptable, keep the extension paired only for intended use, and re-check the active Workday session before agent use.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/chrischall/skills/workday-mcp)
- [npm package](https://www.npmjs.com/package/workday-mcp)
- [workday-mcp source link from artifact](https://github.com/chrischall/workday-mcp)
- [fetchproxy extension source link from artifact](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown setup guidance and structured JSON MCP responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Workday access through the user's active browser session; selected deep-read tools support compact and full views, and raw fetch responses can be bounded by maxBytes.]

## Skill Version(s):

0.6.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
