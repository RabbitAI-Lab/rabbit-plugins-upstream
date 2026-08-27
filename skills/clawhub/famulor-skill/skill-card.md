## Description:

Operate a Famulor workspace through its hosted MCP server, including assistants, conversation history, campaigns, messaging, telephony, knowledge, dashboards, automations, billing, settings, reseller administration, migrations, and long-running tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bekservice](https://clawhub.ai/user/bekservice)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external operators, and developers use this skill to inspect and operate real Famulor workspace resources through the hosted MCP server. It supports assistant configuration, conversation history, campaigns, messaging, telephony, knowledge, dashboards, automations, billing, settings, reseller administration, migrations, and long-running task workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate real workspace data and supports broad administrative workflows.

Mitigation: Install it only for intended Famulor workspaces, connect the smallest relevant MCP toolset, and use least-privilege OAuth scopes.

Risk: Some workflows can trigger destructive, paid, external, or difficult-to-reverse actions such as outreach, live-call control, billing links, phone-number changes, migrations, exports, and persistent automations.

Mitigation: Require explicit approval for the exact target and action, show material cost or irreversible impact when available, and verify completion with read-back or task status.

Risk: Workspace conversations, transcripts, recordings, contacts, customer memories, and message previews may contain personal data.

Mitigation: Retrieve and summarize only what the user needs, respect consent and retention settings, and avoid copying personal data into files or unrelated services.

Risk: Credential and API-key workflows may expose sensitive secrets if handled through chat, commands, logs, or files.

Mitigation: Use OAuth when possible, never ask users to paste secrets into chat, and require a secure handoff before creating or transferring credentials.

## Reference(s):

- [Famulor ClawHub release](https://clawhub.ai/bekservice/skills/famulor-skill)
- [Famulor Skill repository](https://github.com/bekservice/Famulor-Skill)
- [Famulor hosted MCP endpoint](https://app.famulor.io/mcp)
- [Assistant design and onboarding](references/assistant-design.md)
- [Assistants toolset](references/toolsets/assistants.md)
- [Calls toolset](references/toolsets/calls.md)
- [Campaigns toolset](references/toolsets/campaigns.md)
- [Messaging toolset](references/toolsets/messaging.md)
- [Telephony toolset](references/toolsets/telephony.md)
- [Knowledge toolset](references/toolsets/knowledge.md)
- [Dashboards toolset](references/toolsets/dashboards.md)
- [Automations toolset](references/toolsets/automations.md)
- [Billing toolset](references/toolsets/billing.md)
- [Settings toolset](references/toolsets/settings.md)
- [Platform toolset](references/toolsets/platform.md)
- [Migration toolset](references/toolsets/migration.md)
- [Tasks toolset](references/toolsets/tasks.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown and plain text with MCP tool calls or configuration snippets when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should reflect live MCP results and avoid exposing credentials, raw tokens, or unnecessary personal data.]

## Skill Version(s):

2.0.1 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
