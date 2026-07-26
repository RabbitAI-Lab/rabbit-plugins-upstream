## Description: <br>
Baidu Netdisk Skills helps agents manage files in Baidu Netdisk through bdpan commands within the /apps/bdpan app directory, including upload, download, transfer, sharing, search, file organization, and agent memory backup or restore. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent manage Baidu Netdisk files, process share links, organize remote files, and perform supported Claw agent memory backups or restores while observing login, path, and confirmation checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad file-transfer and sharing authority can move, expose, overwrite, or delete Baidu Netdisk files or selected local files. <br>
Mitigation: Require manual approval for uploads, downloads, moves, copies, renames, folder creation, sharing, deletion, restore actions, and background downloads; verify exact source and destination paths before execution. <br>
Risk: Agent memory restore can overwrite existing memory files. <br>
Mitigation: Require an explicit restore date and user approval, list affected files before restore, and keep the documented safety backup before overwriting. <br>
Risk: Background downloads can continue after the active agent turn. <br>
Mitigation: Require approval before starting nohup downloads, surface the process ID and log path, poll progress, and clean up logs after completion. <br>
Risk: Baidu Netdisk credential or configuration exposure could reveal sensitive access tokens. <br>
Mitigation: Do not read or print bdpan configuration or access-token files, and run login or update flows only after user approval. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/baidu-netdisk-skills) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and command-result summaries; some bdpan operations may return JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local or remote file paths, share links, progress logs, execution status, and error guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
