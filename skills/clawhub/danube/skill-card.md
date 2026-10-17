## Description:

Guides agents to discover, inspect, and use an organization's Danube tools and services through MCP or REST, with consent before actions that change data or incur costs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Danube to find and call authorized organizational and catalog tools, inspect their requirements, and manage workflows through an API key or MCP connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Danube credential may grant access to connected tools, services, workflows, skills, context, and wallet features.

Mitigation: Use a narrowly scoped API key where possible and review account permissions before installing.

Risk: The skill instructs agents to save some service parameter defaults without prior approval.

Mitigation: Require explicit user approval before persisting defaults or making other changes.

Risk: Tool calls can change data or initiate spending.

Mitigation: Show the exact action and parameters, then obtain explicit approval before writes or spending.

## Reference(s):

- [Danube REST API guide](references/rest-api.md)
- [Danube troubleshooting](references/troubleshooting.md)
- [Danube documentation](https://docs.danubeai.com)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube on ClawHub](https://clawhub.ai/preston-thiele/skills/danube)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with command and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool results depend on the connected Danube account and its permissions.]

## Skill Version(s):

8.1.36 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
