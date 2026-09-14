## Description:

Sunsama MCP integration with managed authentication for managing daily tasks, calendar events, backlog, objectives, time tracking, and email threads from connected Gmail or Outlook accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to let an agent work with their Sunsama account for daily planning, task search and updates, calendar scheduling, time tracking, and email-thread operations. It is intended for authenticated Maton-connected accounts where users approve new connections, writes, deletes, and hosted automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, move, or delete Sunsama tasks, calendar events, recurring task instances, and email-thread state.

Mitigation: Default to read and list calls first, verify the target resource and payload, and get explicit user approval before every create, update, delete, RSVP, email, or bulk recurring-task operation.

Risk: Raw HTTP fallback can require a long-lived Maton API key that may leak through environment variables, logs, shell history, or child processes.

Mitigation: Prefer OAuth through the Maton CLI and operating-system credential storage; use raw HTTP only when the CLI cannot be installed and keep any API key scoped, temporary, and out of logs.

Risk: Hosted functions, triggers, and trigger destinations can continue running or forwarding event data after setup.

Mitigation: Use user-reviewed function code, prefer DENY_ALL network policy, disclose exact destinations and data flow, require separate approval for persistent automation, and remove functions or destinations when no longer needed.

Risk: The connected account may expose more Sunsama or linked email data than the immediate task needs.

Mitigation: Choose the narrowest available OAuth scopes, connect only accounts needed for the task, and revoke unused or stale connections.

## Reference(s):

- [ClawHub sunsama Skill](https://clawhub.ai/byungkyu/skills/sunsama)
- [Maton](https://maton.ai)
- [Maton Documentation](https://docs.maton.ai)
- [Sunsama](https://sunsama.com)
- [Sunsama Skill Source](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request payloads, and schema references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are authenticated through a user's Maton connection and include confirmation guidance for account-changing actions.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
