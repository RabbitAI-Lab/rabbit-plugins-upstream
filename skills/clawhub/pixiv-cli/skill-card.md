## Description: <br>
Operates Pixiv through the pixiv-cli binary to search illustrations, novels, and users; inspect Pixiv artwork or user IDs/URLs; view rankings and recommendations; manage bookmarks/follows; and download works. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flanchanxwo](https://clawhub.ai/user/flanchanxwo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to guide an agent through Pixiv discovery, account operations, bookmarking/following, downloads, installation, and troubleshooting with the pixiv-cli command line tool. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pixiv refresh tokens and authentication export bundles are plaintext secrets and can be exposed through chat, command arguments, stdout, logs, or transcripts. <br>
Mitigation: Use documented import/export workflows, avoid echoing or summarizing secrets, prefer private files or direct pipelines, and require explicit confirmation before any bare stdout export. <br>
Risk: Downloads write files to disk and user or series URLs can expand to many visual works. <br>
Mitigation: Confirm the destination directory, exact targets, and expanded scope immediately before each download invocation; treat approval as single-use. <br>
Risk: Bookmark, follow, account selection, configuration, update, install, and MCP server operations can change account state, local configuration, binaries, or start a long-running process. <br>
Mitigation: Run these actions only on explicit user request, state the target or change before execution, and require confirmation for account/config state changes and real updates. <br>
Risk: Pixiv CLI errors, authentication requirements, anonymous fallback behavior, and filtered result limits can be misread as empty or complete results. <br>
Mitigation: Check process exit status before parsing output, report real stderr causes, verify command-specific flags with help, and describe bounded results as the first N matches unless exhaustion is shown. <br>


## Reference(s): <br>
- [pixiv-cli repository](https://github.com/FlanChanXwO/pixiv-cli) <br>
- [Authentication import and export](references/auth.md) <br>
- [Discovery playbooks](references/discover.md) <br>
- [Download workflows](references/download.md) <br>
- [Explicit installation workflow](references/install.md) <br>
- [Troubleshooting decision tree](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, CLI output summaries, and local file path reporting when downloads are produced] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May initiate Pixiv account actions, downloads, configuration changes, CLI installation or update, and long-running MCP server startup only when explicitly requested.] <br>

## Skill Version(s): <br>
0.10.0 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
