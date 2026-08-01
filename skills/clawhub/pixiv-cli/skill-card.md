## Description: <br>
Operate Pixiv through the pixiv-cli binary to search illustrations, novels, and users; inspect Pixiv works or user identifiers; view rankings and recommendations; manage bookmarks and follows; and download works when the user explicitly requests a Pixiv operation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flanchanxwo](https://clawhub.ai/user/flanchanxwo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to guide an agent through Pixiv CLI workflows for discovery, account-aware operations, and downloads. It is intended for explicit Pixiv requests and emphasizes command help checks, credential handling, confirmations for account-changing actions, and controlled download behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authentication import or export can expose Pixiv refresh tokens or account bundles. <br>
Mitigation: Use credential workflows only when explicitly requested, avoid echoing secrets, and prefer output files or private terminal input over transcript-visible token handling. <br>
Risk: Bookmark, follow, account-selection, configuration, update, and download actions can change account state or local files. <br>
Mitigation: Confirm the target account, action, destination, and scope before execution; do not carry approval from one operation to another. <br>
Risk: Pixiv user URL downloads can expand to every visual work for that user. <br>
Mitigation: State the expansion scope and target directory before invoking downloads, and wait for completion or user cancellation rather than imposing an arbitrary timeout. <br>


## Reference(s): <br>
- [pixiv-cli homepage](https://github.com/FlanChanXwO/pixiv-cli) <br>
- [Authentication import and export](references/auth.md) <br>
- [Discovery workflows](references/discover.md) <br>
- [Download workflows](references/download.md) <br>
- [Explicit installation workflow](references/install.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and local file paths when downloads are produced] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include confirmation prompts for credential, account-changing, installation, and download actions.] <br>

## Skill Version(s): <br>
0.9.1 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
