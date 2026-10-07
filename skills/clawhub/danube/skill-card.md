## Description:

Helps agents discover, inspect, and invoke organizational and catalog tools through Danube over MCP or HTTP, with guidance to confirm consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can find and use tools connected to their Danube workspace and the wider service catalog, while reviewing sensitive actions before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An OAuth connection or Personal workspace approval may expose more organizational tools than expected.

Mitigation: Use a restricted API key with allowed services and tools for least privilege; do not treat OAuth scopes or Personal approval as access boundaries.

Risk: Some consequential actions may not trigger a platform confirmation prompt.

Mitigation: Ask for explicit user approval before writes, spending, credential storage, workspace context changes, or batch execution, even when no prompt appears.

Risk: Tool calls may send sensitive data to external services.

Mitigation: Share only task-required parameters and keep API keys secret.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube REST API reference](references/rest-api.md)
- [Danube troubleshooting](references/troubleshooting.md)
- [Danube on ClawHub](https://clawhub.ai/preston-thiele/skills/danube)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, API calls]

**Output Format:** [Markdown guidance, shell examples, and tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool availability depends on the selected credential and workspace.]

## Skill Version(s):

8.1.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
