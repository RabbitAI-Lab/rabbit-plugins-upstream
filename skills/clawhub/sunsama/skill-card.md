## Description:

Sunsama MCP integration with managed authentication for managing daily tasks, calendar events, backlog, objectives, time tracking, and email threads from connected Gmail and Outlook accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Sunsama through Maton-managed authentication for task planning, calendar scheduling, backlog management, objectives, timers, and email-thread workflows. It supports direct Sunsama actions and optional user-approved automations through hosted functions and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth authorization can allow the agent to affect real Sunsama tasks, calendars, timers, channels, and linked email threads.

Mitigation: Use read and list operations first, require explicit user confirmation for writes or new connections, and rely on provider-enforced authorization for the connected account.

Risk: Optional hosted functions, triggers, and destinations can continue running or forwarding event data after setup.

Mitigation: Create automations only after separate user approval, keep destinations limited to approved Maton endpoints unless the user names another host, and remove unused connections, functions, or triggers.

Risk: Long-lived API keys and raw responses can expose sensitive task, calendar, or email-thread data.

Mitigation: Prefer OAuth via the Maton CLI credential store, avoid exporting API keys except when the CLI cannot be installed, and return only the fields needed for the user's task.

## Reference(s):

- [ClawHub Sunsama Skill](https://clawhub.ai/byungkyu/skills/sunsama)
- [Maton](https://maton.ai)
- [Sunsama](https://sunsama.com)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Catalog](references/time/triggers.md)
- [Google Mail Trigger Catalog](references/google-mail/triggers.md)
- [Slack Trigger Catalog](references/slack/triggers.md)
- [GitHub Trigger Catalog](references/github/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with inline bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Maton CLI commands, raw HTTP examples, Sunsama MCP tool names, and JSON response shapes.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
