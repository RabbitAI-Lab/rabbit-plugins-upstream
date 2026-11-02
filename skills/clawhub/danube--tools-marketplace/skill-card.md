## Description:

Governed tool access for your agent — one Danube API key unlocks your organization's own tools plus a large, growing catalog of ready-made services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Danube to discover available services, inspect tool schemas, and call organization or catalog tools through MCP or REST with user approval for consequential actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may permit unapproved changes to saved service targets.

Mitigation: Require explicit confirmation and review existing values before saving or replacing a target.

Risk: Scheduled jobs may use the author's credentials without the connecting API key's restrictions, and other people may edit scheduled inputs.

Mitigation: Keep scheduling disabled unless the credential scope and who can edit scheduled inputs are understood and accepted.

Risk: Actions in the wrong workspace or with an overly broad API key can affect unintended resources.

Mitigation: Use a narrowly scoped API key and deliberately select the intended workspace.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [REST API reference](references/rest-api.md)
- [Troubleshooting guide](references/troubleshooting.md)
- [Danube dashboard](https://danubeai.com/dashboard)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands, Configuration]

**Output Format:** [Markdown guidance, JSON API responses, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses and actions depend on the user's connected services, workspace, and API-key permissions.]

## Skill Version(s):

8.1.43 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
