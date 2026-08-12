## Description:

Read-only MCP skill that lets an agent read a user's signed-in Workday tasks, pay, benefits, and compensation data through workday-mcp and the fetchproxy browser extension.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and their agents use this skill to list Workday apps, read tasks or HR data cards, and check bridge/session health from the user's own signed-in Workday session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read sensitive Workday HR, pay, benefits, and compensation details from a signed-in browser session.

Mitigation: Install it only for approved use, limit it to the user's own tenant and session, and follow the employer's acceptable-use policy.

Risk: The skill depends on a paired browser extension and a live Workday SSO session.

Mitigation: Use the healthcheck and pairing prompts to confirm the bridge, extension connection, and Workday session before reading data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-mcp)
- [workday-mcp npm package](https://www.npmjs.com/package/workday-mcp)
- [fetchproxy extension setup dependency](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [JSON, Guidance, Configuration]

**Output Format:** [Structured JSON from MCP tool responses plus plain-English healthcheck status hints.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; responses reflect the user's signed-in Workday session, tenant configuration, and available Workday data.]

## Skill Version(s):

0.3.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
