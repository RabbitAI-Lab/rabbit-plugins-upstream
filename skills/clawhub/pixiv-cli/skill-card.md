## Description:

Operate Pixiv through the pixiv-cli binary to search illustrations, novels, and users; reverse-search images; inspect artwork and user records; view rankings and recommendations; manage bookmarks and follows; and download works.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flanchanxwo](https://clawhub.ai/user/flanchanxwo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent operate the pixiv CLI for Pixiv discovery, account-aware content actions, and downloads while following documented confirmation and credential-handling rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth refresh tokens and authentication export bundles may expose Pixiv account access if echoed, logged, or copied into chat.

Mitigation: Use credential import and export only for explicit user requests, prefer file or direct pipeline workflows, and avoid repeating secret values in commentary or results.

Risk: Bookmark, follow, account selection, configuration, update, and install commands can change account or local system state.

Mitigation: Require explicit user confirmation for each state-changing operation and state the target account, work, user, setting, or install action before execution.

Risk: Whole-user downloads and batch downloads can retrieve large sets of Pixiv content to disk.

Mitigation: Confirm the destination directory and exact targets before each download invocation, and make clear when a URL expands to every visual work in scope.

Risk: Reverse-image search may upload a local image or URL content to SauceNAO or ascii2d.

Mitigation: Use reverse-image providers only for images the user is authorized to share, and respect provider-specific credential and upload constraints.

## Reference(s):

- [Authentication import and export](references/auth.md)
- [Discovery playbooks](references/discover.md)
- [Download workflows](references/download.md)
- [Explicit installation workflow](references/install.md)
- [Troubleshooting decision tree](references/troubleshooting.md)
- [Project homepage](https://github.com/FlanChanXwO/pixiv-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and CLI output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to run pixiv CLI commands that return text, JSON, NDJSON, or local download paths depending on the requested operation.]

## Skill Version(s):

1.0.0 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
