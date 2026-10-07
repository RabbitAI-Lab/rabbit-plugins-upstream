## Description:

Helps agents read Workday org charts, worker profiles, compensation, benefits, performance, and task data through a user's signed-in session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees with authorized Workday access use this skill to ask an agent about their organization, worker profiles, pay, benefits, performance, and other readable Workday pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A signed-in session may expose sensitive HR records, including coworkers' compensation, benefits, or performance data.

Mitigation: Confirm employer policy permits automated access and require explicit intent before retrieving non-self or sensitive records.

## Reference(s):

- [Workday MCP on ClawHub](https://clawhub.ai/chrischall/skills/workday-mcp)
- [Workday MCP npm package](https://www.npmjs.com/package/workday-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown summaries based on structured Workday JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; results depend on the signed-in user's Workday permissions and may contain sensitive HR data.]

## Skill Version(s):

1.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
