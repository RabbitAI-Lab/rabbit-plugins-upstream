## Description:

Google Tasks API integration with managed OAuth for reading, creating, updating, and deleting task lists and tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage Google Tasks through Maton-authenticated CLI or HTTP calls. It supports routine task and task-list operations, with read/list calls as the default and explicit user confirmation before writes, deletions, new connections, or automation setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Tasks data or OAuth/API credentials may be exposed if credentials or raw responses are handled carelessly.

Mitigation: Prefer OAuth, rely on the operating system credential store, avoid exporting long-lived API keys, and display or store only the response fields needed for the user's task.

Risk: Write, delete, or connection-management commands can change task data or revoke access.

Mitigation: Default to read and list operations, then confirm the exact write, deletion, or connection action with the user before execution.

Risk: Hosted functions and triggers can turn a one-off Google Tasks operation into ongoing automation.

Mitigation: Treat functions, triggers, destinations, and exec watches as separate automation decisions that require explicit review of the code, connection, network policy, and data flow.

## Reference(s):

- [Google Tasks Skill Page](https://clawhub.ai/byungkyu/skills/google-tasks-api)
- [Maton Homepage](https://maton.ai)
- [Google Tasks API Overview](https://developers.google.com/workspace/tasks)
- [Tasks Reference](https://developers.google.com/workspace/tasks/reference/rest/v1/tasks)
- [TaskLists Reference](https://developers.google.com/workspace/tasks/reference/rest/v1/tasklists)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Google Mail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, API calls]

**Output Format:** [Markdown instructions with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the user's Maton-authenticated Google Tasks connection and may produce or display task and task-list data returned by the API.]

## Skill Version(s):

1.2.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
