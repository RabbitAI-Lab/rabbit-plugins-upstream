## Description: <br>
Operate Pixiv through the pixiv-cli binary for search, artwork and user inspection, rankings and recommendations, bookmark and follow management, and downloads when the user gives a clear Pixiv context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flanchanxwo](https://clawhub.ai/user/flanchanxwo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to operate the Pixiv CLI for Pixiv discovery, account-aware actions, and controlled downloads while following command-specific safety rules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pixiv refresh tokens and authentication export bundles are plaintext secrets that can be exposed through chat, command output, shell history, or logs. <br>
Mitigation: Use explicit import/export workflows, prefer private files or direct secret-manager pipelines, warn before any raw stdout export, and never repeat or summarize token material. <br>
Risk: Bookmark, follow, account selection, configuration, update, and bulk download operations can change account state, local configuration, installed binaries, or disk contents. <br>
Mitigation: Require an explicit user request and confirm the exact account, target IDs, destination, and scope before each action; do not carry approval across commands. <br>
Risk: A Pixiv user URL download can expand to every visual work for that user and may take time or write many files. <br>
Mitigation: Confirm the target directory and expanded scope immediately before running the download, then wait for completion, user cancellation, or a real error. <br>
Risk: Authentication-dependent searches and restricted content can fail or differ between App API and anonymous Web fallback. <br>
Mitigation: Report the actual CLI error, validate authentication only when needed, and do not add cookies, scraping, or silent fallback workarounds. <br>
Risk: Installing or updating the pixiv binary changes files and may alter PATH. <br>
Mitigation: Install or update only on explicit request, use the approved upstream installer, inspect it before execution, and report the installed version and PATH changes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/flanchanxwo/skills/pixiv-cli) <br>
- [pixiv-cli Repository](https://github.com/FlanChanXwO/pixiv-cli) <br>
- [Authentication import and export](references/auth.md) <br>
- [Discovery playbooks](references/discover.md) <br>
- [Download workflows](references/download.md) <br>
- [Explicit installation workflow](references/install.md) <br>
- [Troubleshooting decision tree](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON or NDJSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local file paths after downloads; secrets and authentication export bundles must not be echoed.] <br>

## Skill Version(s): <br>
0.8.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
