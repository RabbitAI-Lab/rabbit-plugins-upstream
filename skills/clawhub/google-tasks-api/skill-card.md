## Description:

Google Tasks API integration with managed OAuth for reading, creating, updating, and deleting task lists and tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to manage Google Tasks task lists and tasks through Maton-managed OAuth. It supports read/list workflows by default and write or automation workflows when the user explicitly approves the action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected Google Tasks account can expose or modify task lists and tasks.

Mitigation: Use OAuth, connect only the needed account, prefer read-only/list operations first, and require explicit approval before any create, update, move, clear, delete, or connection action.

Risk: Long-lived API keys can leak through environment variables, logs, shell history, or pasted output when raw HTTP is used.

Mitigation: Prefer Maton OAuth through the CLI; when raw HTTP is unavoidable, keep the API key in the process environment only, never print or persist it, and send it only to api.maton.ai.

Risk: Hosted functions and trigger destinations can create persistent automation or forwarding beyond a one-time API call.

Mitigation: Approve each function, trigger, and destination separately, keep destinations inside Maton unless the user explicitly trusts the external host, and delete unused connections, functions, triggers, and destinations when finished.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-tasks-api)
- [Maton Homepage](https://maton.ai)
- [Google Tasks API Overview](https://developers.google.com/workspace/tasks)
- [Google Tasks Tasks Reference](https://developers.google.com/workspace/tasks/reference/rest/v1/tasks)
- [Google Tasks TaskLists Reference](https://developers.google.com/workspace/tasks/reference/rest/v1/tasklists)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user approval before writes, new connections, hosted automation, or persistent trigger destinations.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
