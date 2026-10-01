## Description:

Helps an agent read Workday org charts, worker profiles, compensation, benefits, performance, and other available HR pages through a signed-in session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and authorized teams use this skill to ask an agent for information available in their signed-in Workday session, including reporting chains, profiles, pay, benefits, and performance records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A signed-in Workday session may expose sensitive HR records, including coworkers' pay or performance information.

Mitigation: Treat results as sensitive; check employer policy and access coworker records only with explicit authorization.

Risk: The MCP server and browser extension can read through the live Workday session.

Mitigation: Install only if comfortable with that access, and review the npm package and bridge extension source before use.

## Reference(s):

- [Workday MCP on ClawHub](https://clawhub.ai/chrischall/skills/workday-mcp)
- [workday-mcp npm package](https://www.npmjs.com/package/workday-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [Structured JSON and text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results depend on the signed-in session's access; some tables may return only a first page.]

## Skill Version(s):

1.1.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
