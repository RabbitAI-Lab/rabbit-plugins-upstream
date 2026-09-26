## Description:

Connects agents to an organization's tools and Danube's service catalog for discovery and governed execution over MCP or HTTP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can discover available organizational and third-party tools, inspect their requirements, and run approved actions through Danube.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Danube API key can grant access to many connected third-party and organizational tools.

Mitigation: Use a restricted API key and connect only services needed for the task.

Risk: Tool calls or batches can change data, send messages, spend money, or store credentials.

Mitigation: Enable Danube confirmation where available and obtain explicit user approval for each write, batch, purchase, or credential-storage action.

Risk: Unnecessary personal information or secrets may be shared with connected services.

Mitigation: Send only task-required data and never forward raw secrets or unrelated profile details.

## Reference(s):

- [Danube skill listing](https://clawhub.ai/danube/skills/tools-marketplace)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [REST API reference](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples and summarized tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include confirmation prompts and structured tool results.]

## Skill Version(s):

8.1.14 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
