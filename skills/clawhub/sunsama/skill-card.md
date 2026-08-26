## Description:

Sunsama MCP integration with managed authentication for managing daily tasks, calendar events, backlog, objectives, time tracking, and Gmail or Outlook email threads through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Sunsama planning workflows through authenticated Maton CLI or API calls, including reading tasks and making approved changes to tasks, calendar events, timers, objectives, backlog items, recurring tasks, and linked email threads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized Sunsama access can read and modify tasks, calendar items, and linked Gmail or Outlook email threads.

Mitigation: Install only when that access is acceptable, prefer OAuth, scope the connection narrowly when possible, and confirm the intended Maton profile or connection before use.

Risk: Write, delete, scheduling, and email-thread operations can change real user data.

Mitigation: Require explicit user confirmation before creating, moving, deleting, marking, or otherwise modifying tasks, calendar entries, recurring items, or email threads.

Risk: Multiple Maton profiles or Sunsama connections can cause actions to target the wrong account.

Mitigation: Specify the intended profile and connection when there is any ambiguity, and verify resource identifiers before performing changes.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton API Documentation](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Sunsama](https://sunsama.com)
- [ClawHub Sunsama Skill](https://clawhub.ai/byungkyu/skills/sunsama)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands, JSON request and response examples, and SDK snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, an authorized Sunsama MCP connection, and explicit user confirmation before write or destructive operations.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
