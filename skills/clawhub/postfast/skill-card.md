## Description:

Schedule and manage social media posts across TikTok, Instagram, Facebook, X (Twitter), YouTube, LinkedIn, Threads, Bluesky, Pinterest, Telegram, and Google Business Profile using the PostFast API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[peturgeorgievv](https://clawhub.ai/user/peturgeorgievv)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agencies, and marketing operators use this skill to schedule, draft, publish, analyze, and moderate social media content through PostFast's hosted API. It is suited to cross-platform social workflows that require account listing, media uploads, platform-specific posting controls, analytics, follower history, connect links, or inbox comment actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a PostFast workspace API key and connected social accounts.

Mitigation: Install only when PostFast is trusted with those accounts and keep POSTFAST_API_KEY out of chat transcripts, logs, and rendered examples.

Risk: Publishing, deleting scheduled posts, hiding or deleting comments, and sending Instagram private replies can affect live public accounts.

Mitigation: Review the target account, content, schedule, and action before execution, and require explicit confirmation for destructive or public-facing actions.

Risk: Connect links can attach social accounts to a workspace.

Mitigation: Treat connect links like credentials, scope them to the intended platforms when possible, and share them only with the intended recipient.

## Reference(s):

- [PostFast homepage](https://postfa.st)
- [ClawHub skill page](https://clawhub.ai/peturgeorgievv/skills/postfast)
- [API Reference](references/api-reference.md)
- [Media Upload Flow](references/upload-flow.md)
- [Platform-Specific Controls Reference](references/platform-controls.md)
- [Media Specifications by Platform](references/media-specs.md)
- [PostFast Skill Examples](examples/EXAMPLES.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, API calls]

**Output Format:** [Markdown with inline bash commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires POSTFAST_API_KEY and may produce PostFast API requests that affect connected social accounts.]

## Skill Version(s):

1.17.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
