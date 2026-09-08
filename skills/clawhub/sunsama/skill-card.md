## Description:

Sunsama MCP integration with managed authentication for managing daily tasks, calendar events, backlog, objectives, time tracking, and email threads from connected Gmail or Outlook accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users use this skill to let an agent help plan and update Sunsama work items, calendars, timers, weekly objectives, backlog entries, and connected email-thread follow-ups. It is intended for authenticated Sunsama workflows mediated through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton mediates access to the user's Sunsama account and connected calendar or email data.

Mitigation: Install only when this mediation is acceptable, prefer OAuth over API keys, and use the intended Maton profile and Sunsama connection.

Risk: Write and deletion operations can change or remove Sunsama tasks, calendar events, recurring task instances, and email threads.

Mitigation: Confirm every write or deletion with the user before execution, including the target resource and intended effect.

Risk: Multiple Maton profiles or Sunsama connections can route actions to the wrong account.

Mitigation: Pin the intended Maton profile and Sunsama connection whenever more than one account or connection is available.

## Reference(s):

- [Sunsama](https://sunsama.com)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/sunsama)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI commands, Sunsama MCP endpoint paths, and JSON payloads for task, calendar, backlog, objective, timer, preference, recurring task, and email-thread operations.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
