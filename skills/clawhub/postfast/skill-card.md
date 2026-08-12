## Description:

Schedule and manage social media posts across TikTok, Instagram, Facebook, X (Twitter), YouTube, LinkedIn, Threads, Bluesky, Pinterest, Telegram, and Google Business Profile using the PostFast API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[peturgeorgievv](https://clawhub.ai/user/peturgeorgievv)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing teams use this skill to schedule, draft, cross-post, upload media, inspect analytics, and manage social inbox conversations through the PostFast API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a PostFast workspace API key that can schedule and publish content, upload media, read inbox comments, send replies, and perform moderation actions on connected social accounts.

Mitigation: Install only when that access is acceptable, scope the key to the intended workspace, and require explicit review before posting or replying.

Risk: Public posts, private replies, and moderation actions can affect live social accounts; deletes are irreversible where supported.

Mitigation: Prefer drafts or reversible hide actions for uncertain cases and require explicit approval before irreversible deletes.

## Reference(s):

- [PostFast homepage](https://postfa.st)
- [ClawHub skill page](https://clawhub.ai/peturgeorgievv/skills/postfast)
- [PostFast API Reference](artifact/references/api-reference.md)
- [Media Upload Flow](artifact/references/upload-flow.md)
- [Media Specifications by Platform](artifact/references/media-specs.md)
- [Platform-Specific Controls Reference](artifact/references/platform-controls.md)
- [PostFast Skill Examples](artifact/examples/EXAMPLES.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Configuration]

**Output Format:** [Markdown with curl commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires POSTFAST_API_KEY for authenticated PostFast API calls.]

## Skill Version(s):

1.16.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
