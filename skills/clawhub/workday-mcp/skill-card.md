## Description:

Workday MCP lets an agent read Workday org charts, worker profiles, pay, benefits, compensation, performance, and task or data cards through a signed-in Workday browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and authorized Workday users use this skill to let an agent retrieve Workday people, organization, compensation, benefits, performance, and task data available to their signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive Workday HR data available to the signed-in browser session.

Mitigation: Review before installing, use only with an intended Workday account and tenant, and treat results as potentially including any Workday data that session is authorized to read.

Risk: The setup instructions use remote MCP and browser-extension components.

Mitigation: Pin and verify the MCP package and fetchproxy extension source before use.

Risk: Raw fetch and GraphQL escape-hatch tools may return broader or less-modeled Workday data.

Mitigation: Avoid those tools unless the user understands exactly what Workday data the request may return.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-mcp)
- [npm package referenced by artifact](https://www.npmjs.com/package/workday-mcp)
- [Source repository referenced by artifact](https://github.com/chrischall/workday-mcp)
- [Fetchproxy extension source referenced by artifact](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, JSON]

**Output Format:** [Structured JSON responses with text guidance from the selected Workday tool.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only behavior is described by the artifact; returned data scope depends on what the signed-in Workday session can access.]

## Skill Version(s):

0.6.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
