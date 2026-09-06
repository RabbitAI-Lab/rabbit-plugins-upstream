## Description:

Operates Pixiv through the pixiv-cli binary for authenticated discovery, reverse image search, account actions, bookmarks, follows, and downloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flanchanxwo](https://clawhub.ai/user/flanchanxwo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when a user explicitly asks for Pixiv or pixiv-cli work, so the agent can verify CLI syntax, run Pixiv searches and detail lookups, manage account-backed actions, and handle downloads with consent gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential import or export can expose Pixiv refresh tokens or account bundles.

Mitigation: Use the documented consent and private-output workflows, avoid echoing or summarizing secrets, and prefer file output or authorized direct pipelines when moving credentials.

Risk: Bookmark, follow, full-user download, update, and install operations can change account state, disk state, or the installed binary.

Mitigation: Confirm the exact target, scope, destination, and requested action before execution; treat approvals as single-use.

Risk: Reverse-image searches may upload an image or URL to third-party services such as SauceNAO or ascii2d.

Mitigation: Use only images or URLs the user is authorized to share, disclose the provider upload behavior, and avoid logging source URLs, API keys, or provider response bodies.

## Reference(s):

- [pixiv-cli project homepage](https://github.com/FlanChanXwO/pixiv-cli)
- [Authentication import and export](artifact/references/auth.md)
- [Discovery playbooks](artifact/references/discover.md)
- [Download workflows](artifact/references/download.md)
- [Explicit installation workflow](artifact/references/install.md)
- [Troubleshooting decision tree](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON or NDJSON handling notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes consent gates for credential transfer, account writes, downloads, installation, updates, and reverse-image searches.]

## Skill Version(s):

1.0.1 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
