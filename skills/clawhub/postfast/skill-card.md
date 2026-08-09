## Description:

PostFast helps agents schedule, manage, analyze, and moderate social media content across TikTok, Instagram, Facebook, X, YouTube, LinkedIn, Threads, Bluesky, Pinterest, Telegram, and Google Business Profile using the PostFast API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[peturgeorgievv](https://clawhub.ai/user/peturgeorgievv)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and operators use this skill to create drafts or scheduled posts, upload media, cross-post campaigns, inspect analytics, and manage social inbox comments across connected PostFast accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents through publishing or scheduling public social media content across connected accounts.

Mitigation: Confirm the target account, platform, content, media, and scheduled time before issuing create or publish requests; use PostFast drafts when the user has not clearly approved publication.

Risk: The skill covers moderation actions, including irreversible public-content deletion.

Mitigation: Require explicit user approval for the exact post or comment before deletion; prefer hiding or drafting when deletion is not clearly requested.

Risk: The skill requires a PostFast API key that can access connected social accounts.

Mitigation: Treat POSTFAST_API_KEY as sensitive, keep it out of generated content and logs, and rotate it if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/peturgeorgievv/skills/postfast)
- [PostFast homepage](https://postfa.st)
- [PostFast API Reference](artifact/references/api-reference.md)
- [Platform-Specific Controls Reference](artifact/references/platform-controls.md)
- [Media Upload Flow](artifact/references/upload-flow.md)
- [Media Specifications by Platform](artifact/references/media-specs.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API endpoints, JSON request bodies, and curl command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a POSTFAST_API_KEY environment variable and may produce instructions for public posting, scheduling, moderation, deletion, and analytics workflows.]

## Skill Version(s):

1.16.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
