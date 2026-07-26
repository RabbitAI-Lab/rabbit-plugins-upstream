## Description: <br>
Guides an agent through basic Baidu Netdisk file listing, upload, and small-download workflows using bdpan within the /apps/bdpan/ scope. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent inspect Baidu Netdisk contents, upload local files, and download files up to 50 MB while keeping operations scoped to /apps/bdpan/. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to run bdpan commands that upload, download, or overwrite Baidu Netdisk content. <br>
Mitigation: Require explicit user confirmation before uploads, overwrites, or downloads to sensitive local paths, and keep remote operations within /apps/bdpan/. <br>
Risk: Baidu Netdisk login or configuration data may be sensitive. <br>
Mitigation: Review any installer or login script before use and do not read or output bdpan credential configuration files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/baidu-netdisk-skills-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and concise status guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include confirmation prompts before uploads, overwrites, or downloads to local paths.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
