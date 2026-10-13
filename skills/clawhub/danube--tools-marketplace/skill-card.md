## Description:

Helps agents discover and use an organization's tools and Danube's service catalog through MCP or HTTP, with guidance to confirm consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can search, inspect, and run connected organizational tools and marketplace services using a Danube API key or OAuth connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recommends saving durable parameter defaults without asking the user first.

Mitigation: Require explicit user approval before changing parameter defaults or other account settings.

Risk: A Danube API key or OAuth connection may grant access to connected services and consequential actions.

Mitigation: Prefer a restricted API key over OAuth for least privilege, and confirm every write, send, delete, spend, credential store, workflow, skill, or context change before acting.

## Reference(s):

- [Danube skill on ClawHub](https://clawhub.ai/danube/skills/tools-marketplace)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube documentation](https://docs.danubeai.com)
- [REST API reference](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool responses depend on the connected services and the caller's permissions.]

## Skill Version(s):

8.1.33 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
