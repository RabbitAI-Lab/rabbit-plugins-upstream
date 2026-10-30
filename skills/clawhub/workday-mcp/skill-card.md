## Description:

Read Workday HR data — including org charts, worker profiles, pay, benefits, compensation, performance, and task or data cards — through the user's signed-in session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees with an authorized signed-in Workday session use the skill to retrieve org charts, worker profiles, compensation, benefits, performance, and task data as structured JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed-in Workday access can expose sensitive HR information about colleagues whose records are available to the session.

Mitigation: Use the skill only where employer policy permits sharing the requested HR information with an agent, and limit access to the necessary Workday domains and capabilities.

Risk: External dependency behavior was not fully audited.

Mitigation: Review the package and browser extension, prefer reviewed versions, verify extension checksums, and approve only the required domains and capabilities.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-mcp)
- [workday-mcp package](https://www.npmjs.com/package/workday-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [Structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Workday data; returned free-text content may be untrusted.]

## Skill Version(s):

1.1.11 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
