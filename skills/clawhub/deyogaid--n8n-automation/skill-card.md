## Description:

Manage n8n workflows from OpenClaw via the n8n REST API. Use when the user asks about n8n workflows, automations, executions, or wants to trigger, list, create, activate, or debug n8n workflows. Supports both self-hosted n8n and n8n Cloud instances.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deyogaid](https://clawhub.ai/user/deyogaid)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation operators use this skill to manage n8n workflows, trigger webhooks, and inspect execution status and errors through the n8n REST API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an API key to access workflow and execution data, which may be sensitive and may grant broad permissions.

Mitigation: Use a trusted n8n instance over HTTPS, use a dedicated narrowly scoped API key where available, and protect local key configuration.

Risk: Workflow deletion, activation, webhook execution, or administrative requests can have significant effects in the connected n8n instance.

Mitigation: Require explicit user direction before these actions and confirm the target workflow or endpoint.

Risk: Execution details may contain sensitive information.

Mitigation: Treat execution details as sensitive and share only the information needed for the requested troubleshooting.

## Reference(s):

- [n8n REST API endpoint reference](references/api-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/deyogaid/skills/n8n-automation)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands, Configuration instructions, JSON]

**Output Format:** [Markdown with inline shell commands, HTTP examples, and JSON workflow examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use a user-supplied n8n instance URL and API key.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
