## Description:

Sunsama MCP integration with managed authentication for managing daily tasks, calendar events, backlog, objectives, time tracking, and email threads from connected Gmail or Outlook accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Sunsama through a managed Maton connection for task planning, scheduling, time tracking, and linked email thread workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, delete, or reschedule real Sunsama tasks, calendar events, and linked email threads.

Mitigation: Default to read or list actions, then require explicit user confirmation before any create, update, delete, meeting, or email action.

Risk: Broad account authorization can expose more Sunsama, calendar, or email data than the current task needs.

Mitigation: Prefer OAuth and choose the narrowest available scopes for the specific task.

Risk: Long-lived API keys can leak through environment variables, logs, shell history, or copied output.

Mitigation: Avoid long-lived API keys when OAuth is available, never print or persist credentials, and rotate any key that was exposed.

## Reference(s):

- [Sunsama Skill on ClawHub](https://clawhub.ai/byungkyu/skills/sunsama)
- [Maton](https://maton.ai)
- [Sunsama](https://sunsama.com)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON request or response snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands, raw HTTPS fallback examples, and concise operational guidance for Sunsama actions.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
