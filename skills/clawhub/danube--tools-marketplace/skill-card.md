## Description:

Danube helps agents discover, inspect, and use organization-connected and catalog tools through MCP or curl with a Danube API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to find and run their organization's connected tools and catalog services, with approval before actions that change data or incur costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected tools can give agents broad authority, including actions that modify data or incur charges.

Mitigation: Review account permissions and require explicit approval before side-effecting or paid actions.

Risk: The API key can grant access to connected services and their data.

Mitigation: Install only if you trust Danube with the key and connected services; use appropriately scoped access.

Risk: Profile reads may disclose personal information, and saved parameter defaults may affect later calls.

Mitigation: Avoid profile reads unless needed, and review saved defaults before future executions.

## Reference(s):

- [Danube on ClawHub](https://clawhub.ai/danube/skills/tools-marketplace)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [REST API reference](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool availability and results depend on the connected account and services.]

## Skill Version(s):

8.1.16 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
