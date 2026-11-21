## Description:

Schedule and manage social media posts across supported platforms using the PostFast API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[peturgeorgievv](https://clawhub.ai/user/peturgeorgievv)

### License/Terms of Use:

MIT-0

## Use Case:

Social media teams, creators, and developers use this skill to schedule and manage posts, upload media, connect accounts, and handle supported comment and webhook workflows across social platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports undeclared follower-history and post-analytics features, and scanner coverage is incomplete.

Mitigation: Review whether those analytics features are needed before installing, and limit access to the API key to trusted workflows.

Risk: The skill can guide actions that upload media, schedule or publish posts, reply to comments, and delete posts.

Mitigation: Check the selected account, content, and timing before submitting actions, especially deletions, which the documentation says cannot be undone.

## Reference(s):

- [PostFast](https://postfa.st)
- [PostFast API reference](artifact/references/api-reference.md)
- [Upload flow](artifact/references/upload-flow.md)
- [Social inbox](artifact/references/social-inbox.md)
- [Webhooks](artifact/references/webhooks.md)
- [PostFast ClawHub release](https://clawhub.ai/peturgeorgievv/skills/postfast)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes endpoint and payload examples, workflow steps, and platform-specific constraints.]

## Skill Version(s):

1.21.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
