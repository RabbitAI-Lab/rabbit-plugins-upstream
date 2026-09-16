## Description:

Read Workday HR data, including org charts, worker profiles, pay, benefits, compensation, performance, and task or data cards, through a user's signed-in Workday session via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, managers, and authorized support agents use this skill to retrieve Workday people, compensation, benefits, performance, org chart, app, and task data from their own signed-in Workday session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose highly sensitive Workday HR data, including compensation, benefits, performance, and other-worker records.

Mitigation: Install and invoke it only under an employer-approved policy, limit activation scope, and treat outputs as confidential.

Risk: Broad triggers can activate the skill for many Workday-related requests.

Mitigation: Avoid broad or global activation unless the agent environment lets users control when the skill is invoked.

Risk: The setup uses unpinned install steps for the MCP package and fetchproxy extension.

Mitigation: Pin and review the workday-mcp package and fetchproxy extension before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-mcp)
- [npm package: workday-mcp](https://www.npmjs.com/package/workday-mcp)
- [fetchproxy extension source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command examples; MCP tool calls return structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only. Selected deep-read tools default to compact responses that strip media fields, and raw fetch or GraphQL responses can be bounded by maxBytes.]

## Skill Version(s):

0.6.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
