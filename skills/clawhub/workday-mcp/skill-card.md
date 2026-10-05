## Description:

Helps an agent read Workday org charts, worker profiles, compensation, benefits, performance, and other available pages through the user's signed-in session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and other authorized users can ask an agent to inspect Workday people, team, pay, benefits, and performance information available to their signed-in session. The skill provides read-only access through an installed MCP server and browser extension.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The signed-in Workday session can expose sensitive HR fields, including coworker, compensation, and performance data.

Mitigation: Confirm employer permission and request or share only data you are authorized to access and use.

Risk: Installing the MCP package and browser extension introduces software that can access the signed-in session.

Mitigation: Verify the npm package and browser extension source or release checksums before installation.

## Reference(s):

- [ClawHub workday-mcp release](https://clawhub.ai/chrischall/skills/workday-mcp)
- [workday-mcp npm package](https://www.npmjs.com/package/workday-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [Structured Workday data via MCP and text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; some Workday pages or tables may be incomplete or require additional navigation.]

## Skill Version(s):

1.1.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
