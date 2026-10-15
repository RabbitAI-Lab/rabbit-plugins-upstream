## Description:

Guides employees in reading Workday HR data through their signed-in browser session using the fpx CLI, without a separate MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized employees and developers use this skill to retrieve Workday org charts, worker profiles, tasks, pay, benefits, compensation, and app listings through their existing signed-in session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access through a signed-in browser session can expose confidential HR, pay, benefits, compensation, and worker-profile data.

Mitigation: Use only with organizational authorization, treat results as confidential, and redact personal and compensation fields by default.

Risk: Raw Workday responses may expose a session security token and sensitive employee data.

Mitigation: Project only required fields, avoid raw response logging, and never print the session security token.

Risk: A paired browser bridge may retain access to the signed-in Workday session.

Mitigation: Restrict extension site access and remove or unpair the bridge when it is no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/workday-fpx)
- [Workday endpoint reference](references/endpoints.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only examples project selected fields from JSON responses.]

## Skill Version(s):

1.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
