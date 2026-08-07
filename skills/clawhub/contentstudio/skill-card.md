## Description:

ContentStudio is a tool to schedule social-media posts and manage the social inbox across Facebook, LinkedIn, Twitter/X, Instagram, YouTube, TikTok, Pinterest, Threads, Tumblr, Bluesky, and Google Business Profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[contentstudio-official](https://clawhub.ai/user/contentstudio-official)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and AI-agent users use this skill to manage ContentStudio workspaces from the terminal, including social post scheduling, media management, approval workflows, inbox review, and customer-facing replies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The assistant can operate a ContentStudio account and perform account-changing or customer-facing social media actions.

Mitigation: Install only when this delegation is intended, use a least-privilege API key where possible, and review customer-facing messages before sending.

Risk: Create, update, delete, approve, and reply actions could affect the wrong workspace or social account.

Mitigation: Keep dry-run previews enabled before mutations and confirm the target workspace before executing changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/contentstudio-official/skills/contentstudio)
- [ContentStudio API Guide](https://api.contentstudio.io/guide)
- [ContentStudio API Docs](https://api.contentstudio.io/api-docs)
- [ContentStudio CLI npm Package](https://www.npmjs.com/package/contentstudio-cli)
- [ContentStudio Website](https://contentstudio.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON response handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the ContentStudio CLI and requires CONTENTSTUDIO_API_KEY for authenticated operations.]

## Skill Version(s):

1.1.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
