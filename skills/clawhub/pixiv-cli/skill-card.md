## Description:

Safely operates Pixiv through the pixiv-cli binary for discovery, account actions, reverse image search, and downloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flanchanxwo](https://clawhub.ai/user/flanchanxwo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when an agent must operate Pixiv through pixiv-cli for authenticated searches, Pixiv URL or ID inspection, reverse image search, bookmarks, follows, comments, and download workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate pixiv-cli with the user's Pixiv account, including bookmarks, follows, comments, downloads, and credential maintenance.

Mitigation: Run account-changing, credential, and download actions only for explicit user requests, and state the target and scope before execution.

Risk: Pixiv refresh tokens, auth export bundles, SauceNAO API keys, and FANBOXSESSID values are sensitive secrets.

Mitigation: Keep secrets out of chat, logs, and summaries; use private files, hidden prompts, redacted config reads, or direct authorized pipelines when credentials must move.

Risk: Reverse-image search can share images or image URLs with third-party providers such as SauceNAO or ascii2d.

Mitigation: Use reverse-image search only with local images or URLs the user is authorized to share, and do not echo sources, keys, temporary paths, redirects, or upstream response bodies.

Risk: Download commands can write many files when a Pixiv user or bookmark URL expands into a broad set of works.

Mitigation: Confirm the destination directory, exact targets, and item scope for each download invocation; treat approval as single-use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flanchanxwo/skills/pixiv-cli)
- [Publisher profile](https://clawhub.ai/user/flanchanxwo)
- [pixiv-cli homepage](https://github.com/FlanChanXwO/pixiv-cli)
- [Authentication import and export](references/auth.md)
- [Discovery playbooks](references/discover.md)
- [Download workflows](references/download.md)
- [Explicit installation workflow](references/install.md)
- [Troubleshooting decision tree](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and CLI output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON or NDJSON command output summaries, local file paths after downloads, and configuration guidance; secrets must not be repeated.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
