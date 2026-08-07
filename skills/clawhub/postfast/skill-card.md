## Description:

PostFast helps agents schedule, manage, analyze, and moderate social media posts across TikTok, Instagram, Facebook, X, YouTube, LinkedIn, Threads, Bluesky, Pinterest, Telegram, and Google Business Profile through the PostFast API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[peturgeorgievv](https://clawhub.ai/user/peturgeorgievv)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing operators use this skill to create drafts or scheduled posts, upload media, cross-post campaigns, inspect analytics and follower history, manage connected accounts, and triage social inbox comments through PostFast.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A PostFast API key can let the agent publish, schedule, reply to, moderate, and delete content on connected social accounts.

Mitigation: Install only for agents and workspaces trusted to act on those accounts, and review proposed publishing or moderation actions before execution.

Risk: Delete and moderation actions can affect live platform content, and comment deletion can be irreversible.

Mitigation: Before any delete or moderation action, require the exact post or comment, account, platform, and ID, then ask for explicit confirmation.

## Reference(s):

- [PostFast ClawHub skill page](https://clawhub.ai/peturgeorgievv/skills/postfast)
- [PostFast homepage](https://postfa.st)
- [PostFast API Reference](artifact/references/api-reference.md)
- [Platform-Specific Controls Reference](artifact/references/platform-controls.md)
- [Media Specifications by Platform](artifact/references/media-specs.md)
- [Media Upload Flow](artifact/references/upload-flow.md)
- [PostFast Skill Examples](artifact/examples/EXAMPLES.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires POSTFAST_API_KEY and connected social accounts; outputs may include API calls that publish, schedule, reply to, moderate, or delete social content.]

## Skill Version(s):

1.15.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
