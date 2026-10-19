## Description:

Helps agents discover and use an organization's tools and Danube's service catalog through MCP or REST, with user confirmation before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danube](https://clawhub.ai/user/danube)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Danube to find and invoke organization-connected tools and third-party services, while seeking explicit approval for writes, spending, credential changes, and other consequential operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad tool access can reach services beyond the intended task, and OAuth does not provide narrow tool scoping.

Mitigation: Use a restricted API key with allowed_services and allowed_tools when narrow access is needed; install only when broad gateway access is intended.

Risk: Tool calls can write, send, spend, or expose credentials.

Mitigation: Enable confirmation requirements where available and request explicit user approval for consequential calls, including credential storage and wallet actions.

Risk: Scheduled workflows and updates to context, parameter defaults, skills, or workflows can persist or repeat unintended changes.

Mitigation: Require explicit approval for durable state changes and author review before changing scheduled workflows.

## Reference(s):

- [Danube skill on ClawHub](https://clawhub.ai/danube/skills/tools-marketplace)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [REST API reference](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide external tool calls; consequential actions require explicit user approval.]

## Skill Version(s):

8.1.39 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
