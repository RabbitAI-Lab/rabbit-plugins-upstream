## Description:

Controls a Discord bot for message management, reactions, stickers, custom emoji, polls, threads, pinned messages, search, member and role lookup, voice state checks, scheduled events, and gated moderation actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Community operators, moderators, and developers use this skill to automate Discord announcements, collaboration follow-up, emoji and sticker workflows, polls, threads, and moderation tasks through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact Discord moderation actions, including message deletion, timeout, kick, and ban.

Mitigation: Keep moderation and role gates disabled unless required, use a least-privilege bot token, and require human confirmation before destructive moderation actions.

Risk: A leaked or over-privileged Discord bot token could allow unauthorized posting, role changes, or moderation.

Mitigation: Store tokens outside version control, limit bot permissions to the intended server operations, rotate credentials when exposure is suspected, and avoid logging secrets.

Risk: The server security summary flags broad local exec/read/write claims and vague non-Discord automation scope.

Mitigation: Run the skill in a constrained agent workspace, review requested file and command operations, and restrict local tool access to what the Discord workflow actually needs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/discord)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Configuration guidance, API calls]

**Output Format:** [Markdown guidance and JSON Discord action payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Discord channel, message, user, role, guild, media URL, and action identifiers.]

## Skill Version(s):

1.0.2 (source: server release evidence; artifact frontmatter reports 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
