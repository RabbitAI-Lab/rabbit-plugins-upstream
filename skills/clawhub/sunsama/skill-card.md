## Description:

Sunsama MCP integration that lets agents manage daily tasks, calendar events, backlog, objectives, time tracking, and Gmail or Outlook email threads through Maton-managed authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent plan and update Sunsama work across tasks, calendars, objectives, timers, and connected email threads. It is suited to authenticated account workflows where reads are preferred first and user confirmation gates connection creation and data-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Sunsama account data and connected Gmail, Outlook, and calendar content through Maton.

Mitigation: Install only when the user trusts Maton with those accounts, prefer OAuth, review requested scopes, and connect only accounts needed for the current task.

Risk: Write operations can modify or delete tasks, calendar events, email thread state, recurring tasks, and settings.

Mitigation: Default to read and list calls first, then require clear user confirmation with resource identifiers and intended effects before any change.

Risk: Multiple Maton profiles or Sunsama connections can route an action to the wrong account.

Mitigation: Use explicit profile and connection targeting when more than one account or connection exists.

Risk: Raw HTTP fallback requires handling a long-lived Maton API key in the process environment.

Mitigation: Use the CLI when available; if raw HTTP is necessary, never print, log, persist, or pass the key on a command line, and send it only to api.maton.ai.

## Reference(s):

- [Sunsama](https://sunsama.com)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with CLI commands and JSON request and response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes MCP tool schemas for Sunsama task, calendar, backlog, objective, timer, email, recurring task, and settings operations.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
