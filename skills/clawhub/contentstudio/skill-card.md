## Description:

ContentStudio is a tool to schedule social-media posts, manage the social inbox, and pull performance analytics across Facebook, LinkedIn, Twitter/X, Instagram, YouTube, TikTok, Pinterest, Threads, Tumblr, Bluesky, and Google Business Profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[contentstudio-official](https://clawhub.ai/user/contentstudio-official)

### License/Terms of Use:

MIT

## Use Case:

Social media managers, support teams, developers, and AI agents use this skill to operate ContentStudio workspaces from the terminal: schedule and approve posts, manage accounts and media, triage inbox conversations, and retrieve analytics reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs an unpinned global CLI with broad authority over ContentStudio workspaces and social accounts.

Mitigation: Install only a trusted, verified, and preferably pinned contentstudio-cli version before enabling the skill.

Risk: Mutating commands can delete content, approve posts, alter social accounts, or send customer-facing inbox replies.

Mitigation: Use dry-run previews, confirm the target workspace, and require explicit human approval before destructive or customer-facing actions.

Risk: API keys and base URL overrides can grant access to real ContentStudio accounts or redirect requests to an unintended service.

Mitigation: Use narrowly scoped, revocable API keys; protect local configuration and environment variables; and avoid inherited or untrusted CONTENTSTUDIO_BASE_URL values.

Risk: Bulk-delete and auto-approve examples can cause large unintended changes if run unattended.

Mitigation: Review candidate items first and run bulk deletion or approval workflows only with deliberate human confirmation.

## Reference(s):

- [ContentStudio Skill Page](https://clawhub.ai/contentstudio-official/skills/contentstudio)
- [ContentStudio API Guide](https://api.contentstudio.io/guide)
- [ContentStudio API Docs](https://api.contentstudio.io/api-docs)
- [contentstudio-cli npm Package](https://www.npmjs.com/package/contentstudio-cli)
- [ContentStudio Website](https://contentstudio.io)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON response expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the contentstudio CLI and CONTENTSTUDIO_API_KEY; mutating actions should be previewed with dry-run output and confirmed before execution.]

## Skill Version(s):

1.4.0 (source: frontmatter, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
