## Description:

Helps agents discover, inspect, and run an organization's tools and catalog services through Danube, with user confirmation before sensitive actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Danube to find and run tools available to their organization through MCP or HTTP, while obtaining consent for actions that change data, send information, or spend funds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Danube key may let the agent see and run a broad range of tools.

Mitigation: Use a restricted Danube API key that grants only the needed services and tools.

Risk: OAuth scopes and MCP tool filters do not reliably restrict the agent's permissions.

Mitigation: Do not treat them as permission boundaries; enforce access through a restricted key.

Risk: Tool execution can write, send, spend, store credentials, or change skills, workflows, and context.

Mitigation: Show the exact action and parameters and get explicit user confirmation before proceeding.

## Reference(s):

- [Danube skill release](https://clawhub.ai/danube/skills/tools-marketplace)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube REST API examples](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool results depend on the user's Danube key and available services.]

## Skill Version(s):

8.1.31 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
