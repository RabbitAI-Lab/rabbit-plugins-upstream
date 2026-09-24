## Description:

Microsoft To Do API integration with managed OAuth for managing task lists, tasks, checklist items, and linked resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to read and manage Microsoft To Do lists and tasks through a Maton-authenticated Microsoft connection. It is intended for task management workflows where reads are preferred by default and writes, deletes, new connections, hosted functions, and automation require user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Microsoft To Do data through a user-authorized Maton connection.

Mitigation: Confirm the intended account and connection before use, prefer read/list calls first, and use the narrowest available OAuth scope.

Risk: Write and delete operations can change or remove task data.

Mitigation: Require explicit user confirmation of the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE call.

Risk: Hosted functions and triggers can create ongoing automation or data forwarding.

Mitigation: Review the function code, network policy, trigger scope, and destination URL separately, and get explicit user approval before creating or invoking automation.

Risk: Raw API-key fallback exposes a long-lived Maton credential to the process environment.

Mitigation: Use OAuth through the Maton CLI when possible; when raw HTTP is necessary, never print, persist, log, or pass the API key on a command line.

## Reference(s):

- [Microsoft To Do API Overview](https://learn.microsoft.com/en-us/graph/api/resources/todo-overview)
- [todoTaskList Resource](https://learn.microsoft.com/en-us/graph/api/resources/todotasklist)
- [todoTask Resource](https://learn.microsoft.com/en-us/graph/api/resources/todotask)
- [checklistItem Resource](https://learn.microsoft.com/en-us/graph/api/resources/checklistitem)
- [linkedResource Resource](https://learn.microsoft.com/en-us/graph/api/resources/linkedresource)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Microsoft To Do Skill Page](https://clawhub.ai/byungkyu/skills/microsoft-to-do)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON/API response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected Microsoft To Do account; write, delete, connection, hosted function, and automation actions require explicit user approval.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
