## Description:

智能体Telegram defines Telegram notification conventions for eight agent roles, including account IDs, emoji prefixes, message timing, and standard templates for sending user-facing status updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to standardize Telegram status notifications from multi-agent teams. It is intended for task starts, subtask completion reports, issue escalation, and final summaries sent through a configured Telegram message tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Messages are routed to a fixed Telegram recipient ID.

Mitigation: Confirm the configured recipient is the intended user before enabling the skill, and change or disable the route when operating in another environment.

Risk: Task details, local paths, or internal debugging information may be sent off-platform.

Mitigation: Instruct agents to omit secrets, private file paths, customer data, and sensitive debugging details unless explicitly approved.

Risk: Telegram bot tokens are required for role-specific accounts.

Mitigation: Store bot tokens securely outside the skill content and restrict access to authorized users and agents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agent-telegram)
- [Telegram Bot API](https://api.telegram.org)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands]

**Output Format:** [Markdown guidance with JSON and JavaScript-style message call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defines fixed role-to-account mappings, message templates, and Telegram routing conventions.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
