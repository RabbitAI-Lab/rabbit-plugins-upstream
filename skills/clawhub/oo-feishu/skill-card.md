## Description: <br>
Feishu (feishu.cn). Use this skill for ANY Feishu request - reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to operate Feishu through an OOMOL-connected account for Drive, Docs, Wiki, Sheets, Slides, Base, mail, chat, calendar, tasks, approvals, OKRs, Minutes, and video meeting workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read, create, update, and delete Feishu resources through the connected account. <br>
Mitigation: Install it only when Feishu access through OOMOL is intended, and confirm the exact payload and effect before running write or destructive actions. <br>
Risk: Broad Feishu actions may affect sensitive mail, Drive, Base, Wiki, calendar, approval, and chat data. <br>
Mitigation: Review target identifiers, permissions, recipients, and content before approving state-changing operations. <br>
Risk: Connector action schemas can change over time. <br>
Mitigation: Inspect the live connector schema before building each payload so the command matches the current Feishu action contract. <br>


## Reference(s): <br>
- [Feishu homepage](https://www.feishu.cn) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-feishu) <br>
- [Publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include Feishu action names, schema-inspection commands, connector run commands, confirmation prompts for state-changing actions, and guidance for handling auth or connection failures.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
