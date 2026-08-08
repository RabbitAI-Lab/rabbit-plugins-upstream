## Description:

Schedule and manage social media posts across TikTok, Instagram, Facebook, X (Twitter), YouTube, LinkedIn, Threads, Bluesky, Pinterest, Telegram, and Google Business Profile using the PostFast API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[peturgeorgievv](https://clawhub.ai/user/peturgeorgievv)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketing teams, and automation agents use this skill to create, schedule, review, and manage social media content across connected PostFast accounts. It supports account discovery, media uploads, cross-posting, analytics lookup, follower history, comment inbox triage, replies, moderation actions, and platform-specific posting controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can schedule or publish content to live social channels.

Mitigation: Use a trusted agent workflow that asks for confirmation before scheduling or sending public content, and scope the PostFast API key to acceptable workspaces and accounts.

Risk: The skill exposes public and private reply actions that can represent the account owner.

Mitigation: Require human review for replies, private replies, and social inbox triage where brand, privacy, or customer-support impact matters.

Risk: The skill can delete or moderate public content, and deletion may be irreversible.

Mitigation: Require explicit approval before deleting posts or comments, hiding comments, changing inbox state, or performing other moderation actions.

Risk: Connect links can let clients attach social accounts to a workspace.

Mitigation: Share connect links only with intended recipients and use API keys limited to workspaces where delegated account access is acceptable.

## Reference(s):

- [PostFast ClawHub skill page](https://clawhub.ai/peturgeorgievv/skills/postfast)
- [PostFast homepage](https://postfa.st)
- [PostFast API Reference](references/api-reference.md)
- [Platform-Specific Controls Reference](references/platform-controls.md)
- [Media Specifications by Platform](references/media-specs.md)
- [Media Upload Flow](references/upload-flow.md)
- [PostFast Skill Examples](examples/EXAMPLES.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request bodies and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a PostFast workspace API key in POSTFAST_API_KEY and connected social accounts before live posting actions can succeed.]

## Skill Version(s):

1.15.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
