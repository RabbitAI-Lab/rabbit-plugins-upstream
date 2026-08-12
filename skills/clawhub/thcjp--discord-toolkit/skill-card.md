## Description:

Enterprise Discord administration skill for batch messages, moderation, role permissions, custom emoji and sticker management, multi-channel scheduling, and server information queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External community operators and enterprise Discord administrators use this skill to automate high-volume Discord operations such as announcements, moderation actions, role changes, emoji and sticker uploads, and status queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent powerful Discord server administration authority.

Mitigation: Install only for Discord administration use cases and grant the bot the minimum permissions needed for the intended server operations.

Risk: Moderation, message deletion, and role operations can have high-impact effects on a server.

Mitigation: Keep moderation and role actions disabled until needed, use dry runs where available, and require confirmation for bans, deletions, and role changes.

Risk: The skill's broad local tool permissions and generic wording may expand use beyond Discord administration.

Mitigation: Avoid using it for general file processing or shell automation, and review the local audit log path and retention before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/discord-toolkit)
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON action payloads and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Discord action payloads, execution summaries, error guidance, and audit or permission recommendations.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
