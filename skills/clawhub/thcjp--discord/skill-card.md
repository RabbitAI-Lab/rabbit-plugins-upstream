## Description:

Discord 全能控制 helps an agent operate a Discord bot for message management, reactions, stickers and custom emoji, polls, threads, pinned messages, search, member and role lookup, voice and event status, and gated moderation actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Community operators, moderators, and team automation developers use this skill to automate Discord bot workflows such as publishing notices, tracking discussions, managing polls and threads, and applying carefully gated moderation actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Powerful Discord bot actions can alter messages, roles, or member access if used against the wrong server, channel, or user.

Mitigation: Install only for a bot account with permissions limited to the intended servers and channels, keep role and moderation gates disabled unless needed, and confirm target IDs before deletes, role changes, timeouts, kicks, or bans.

Risk: Media upload and callback workflows can expose sensitive local files or send data to untrusted URLs.

Mitigation: Avoid passing sensitive local files or untrusted callback URLs, and review file paths and URLs before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/discord)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON action examples and shell environment configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Discord action names, target IDs, media URLs, permission checks, status codes, response data, and completion logs.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
