## Description:

Wrike API integration with managed OAuth for managing tasks, folders, projects, spaces, team collaboration, and administrative functions through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to read and manage Wrike work items, collaboration resources, time logs, and account administration through an authenticated Maton connection. It is suited to agent-assisted Wrike workflows where reads are preferred by default and writes, connection creation, admin actions, exports, functions, triggers, and destinations require explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform Wrike writes and account-governance operations through the user's authorized connection.

Mitigation: Default to read/list operations and require explicit user approval with target resource, payload, and intended effect before POST, PUT, PATCH, DELETE, invitations, user management, access-role changes, or workflow changes.

Risk: Audit log access and data export can expose sensitive telemetry or bulk organizational data.

Mitigation: Invoke audit log or data export only after the user explicitly requests it and confirms the scope; extract only task-relevant fields and avoid storing raw responses unless requested.

Risk: Connections, functions, triggers, and destinations can create persistent access or automated forwarding.

Mitigation: Get separate approval for connection creation, function deployment or invocation, trigger creation, and each destination; prefer least-privilege OAuth scopes, DENY_ALL network policy for functions, and named approved hosts for any destination.

Risk: Local event handlers run on untrusted third-party event data.

Mitigation: Use local execution only when the user provides or reviews the handler, parse event input as data, avoid shell interpolation or eval, and confirm that unattended automation is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/wrike-api)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Wrike API Documentation](https://developers.wrike.com/)
- [Wrike API Overview](https://developers.wrike.com/overview/)
- [OAuth 2.0 Authorization](https://developers.wrike.com/oauth-20-authorization/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly trigger reference](references/calendly/triggers.md)
- [GitHub trigger reference](references/github/triggers.md)
- [Google Mail trigger reference](references/google-mail/triggers.md)
- [HubSpot trigger reference](references/hubspot/triggers.md)
- [Linear trigger reference](references/linear/triggers.md)
- [Notion trigger reference](references/notion/triggers.md)
- [Slack trigger reference](references/slack/triggers.md)
- [Stripe trigger reference](references/stripe/triggers.md)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce authenticated Wrike API call patterns and automation guidance; user approval is required before writes, new connections, admin operations, data exports, function deployment, trigger setup, or persistent destinations.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
