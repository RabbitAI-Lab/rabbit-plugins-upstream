## Description:

Build or customize an owner-only proactive companion system with a cyber-girlfriend persona, Markdown private-life context, lightweight relationship memory, and OpenClaw presence cron delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kasanuowa](https://clawhub.ai/user/kasanuowa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to set up an owner-only proactive companion that maintains persona and daily-life context, schedules presence messages, and delivers text or optional media through a configured OpenClaw route.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scheduled outbound companion messages or media may be sent to a configured owner target.

Mitigation: Review the delivery channel, sender account, cron schedules, pacing, and quiet hours before enabling delivery; require explicit confirmation before the first verification message.

Risk: The skill can create local state and use local OpenClaw or WeChat session or credential data for delivery.

Mitigation: Keep runtime-specific values in local configuration or environment variables, maintain owner-only scope, and validate the install before use.

Risk: WeChat fallback behavior may retry delivery when a configured channel cannot be resolved.

Mitigation: Review the fallback route before enabling it and use the reversible pause path when outbound delivery should stop without deleting local state.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kasanuowa/skills/cyber-girlfriend)
- [Standard Init Upgrade Flow](references/standard-init-upgrade-flow.md)
- [Configuration](references/configuration.md)
- [Contract Schema](references/contract-schema.md)
- [First-Time Setup Guide](references/first-time-setup.md)
- [Presence Integration](references/presence-integration.md)
- [Required Events And Cron](references/required-events-and-cron.md)
- [Private Life Layer](references/private-life-layer.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON configuration, shell commands, and local Markdown state files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local companion state and schedule recurring OpenClaw jobs after owner confirmation.]

## Skill Version(s):

2.2.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
