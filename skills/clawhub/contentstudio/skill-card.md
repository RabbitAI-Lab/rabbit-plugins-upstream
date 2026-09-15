## Description:

ContentStudio helps agents schedule social-media posts, manage the social inbox, generate and edit AI images, manage media and accounts, and pull analytics across supported social platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[contentstudio-official](https://clawhub.ai/user/contentstudio-official)

### License/Terms of Use:

MIT

## Use Case:

External developers, marketers, and operators use this skill to automate ContentStudio workspaces from an agent, including post scheduling, inbox handling, media and account management, approvals, AI image workflows, and analytics reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and invokes mutable external CLI code from the ContentStudio npm package.

Mitigation: Install only from the trusted ContentStudio publisher, prefer a pinned CLI version or reviewed package source, and review updates before deployment.

Risk: API keys and connected social accounts can authorize publishing, deletion, approval, customer replies, workspace changes, and paid AI image actions.

Mitigation: Use a least-privilege API key, avoid exposing secrets in shell commands, confirm the target workspace, run dry-run previews where supported, and require explicit approval before high-impact actions.

Risk: Inbox replies and comments can send customer-facing messages with no provider-side undo.

Mitigation: Preview the exact message text and destination, then obtain explicit user approval before sending or deleting customer-facing content.

## Reference(s):

- [ContentStudio Skill on ClawHub](https://clawhub.ai/contentstudio-official/skills/contentstudio)
- [ContentStudio Publisher Profile](https://clawhub.ai/user/contentstudio-official)
- [ContentStudio API Guide](https://api.contentstudio.io/guide)
- [ContentStudio API Docs](https://api.contentstudio.io/api-docs)
- [contentstudio-cli on npm](https://www.npmjs.com/package/contentstudio-cli)
- [ContentStudio Website](https://contentstudio.io)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the contentstudio CLI and CONTENTSTUDIO_API_KEY; mutating workflows are expected to use dry-run previews and explicit approval.]

## Skill Version(s):

1.5.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
