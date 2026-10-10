## Description:

Guides agents to discover and use Danube's organizational and catalog tools over MCP or REST, with user confirmation before actions that write, send, spend, or delete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to connect agents to organizational and public tools, discover suitable operations, and carry out authorized tasks while checking sensitive actions with the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad remote tool authority may expose organization data or allow consequential actions.

Mitigation: Use a manually created API key limited to necessary services and tools; confirm each write, send, spend, credential, skill, workflow, or batch action with the user.

Risk: Documented authorization-scope gaps can make a broad connection unsuitable as an isolation boundary.

Mitigation: Do not rely on OAuth Personal for least-privilege isolation; review permitted tools and credentials before use.

## Reference(s):

- [Danube on ClawHub](https://clawhub.ai/preston-thiele/skills/danube)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [REST API reference](artifact/references/rest-api.md)
- [Troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool availability and responses depend on the user's Danube access.]

## Skill Version(s):

8.1.30 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
