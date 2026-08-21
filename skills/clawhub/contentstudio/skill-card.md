## Description:

ContentStudio is a tool to schedule social-media posts and manage the social inbox across Facebook, LinkedIn, Twitter/X, Instagram, YouTube, TikTok, Pinterest, Threads, Tumblr, Bluesky, and Google Business Profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[contentstudio-official](https://clawhub.ai/user/contentstudio-official)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and AI agents use this skill to operate a ContentStudio workspace from the terminal: schedule or update social posts, manage media and accounts, review approvals, handle inbox activity, and audit workspace resources through the ContentStudio public API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish, delete, approve, moderate, and edit ContentStudio account data when it has an API key.

Mitigation: Install it only for trusted agents, use the minimum needed API-key permissions, and require dry-runs plus explicit approval before mutating account resources.

Risk: Actions may affect the wrong workspace if the active workspace is assumed.

Mitigation: Confirm the target workspace before mutating actions and pass an explicit workspace when the action is a one-off.

Risk: Inbox replies, comments, reviews, and deletes can be customer-facing or difficult to undo.

Mitigation: Preview the exact outgoing text or destructive action with dry-run behavior and get explicit user approval before sending or deleting.

## Reference(s):

- [ContentStudio Skill Page](https://clawhub.ai/contentstudio-official/skills/contentstudio)
- [ContentStudio API Guide](https://api.contentstudio.io/guide)
- [ContentStudio API Docs](https://api.contentstudio.io/api-docs)
- [contentstudio-cli npm Package](https://www.npmjs.com/package/contentstudio-cli)
- [ContentStudio Website](https://contentstudio.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON response conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the contentstudio CLI and CONTENTSTUDIO_API_KEY; mutating actions should use dry-run checks and explicit user approval.]

## Skill Version(s):

1.2.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
