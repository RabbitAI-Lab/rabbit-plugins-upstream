## Description: <br>
当用户要换电脑、切换设备或在另一台机器继续开发时，帮助把当前 WorkBuddy 项目和工作现场（未提交改动、Git、项目内配置、Agent 规则/Skill 与交接上下文）安全打包成加密工作包，或恢复已有 .wbpack 并接着上次工作。适用于“跨设备项目迁移/接力”“工作现场打包/恢复”“把项目和 Agent 上下文一起带走”等请求；不把单纯云同步、实时多人协作、普通 Git 同步或部署作为主要场景。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[taogeo](https://clawhub.ai/user/taogeo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers using WorkBuddy use this skill to move an active project workspace between devices by creating an encrypted .wbpack that preserves project files, Git data, project-local configuration, Agent rules, Skills, and handoff context, or by restoring a trusted .wbpack without overwriting existing work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workspace package can include project-local secrets such as .env files and Git history. <br>
Mitigation: Treat generated .wbpack files as confidential, use a strong password, and transfer or store them only through trusted channels. <br>
Risk: Restoring a package from an untrusted source could place unwanted or harmful project files in the workspace. <br>
Mitigation: Restore packages only from sources the user trusts; the workflow validates the archive and does not automatically execute restored files. <br>
Risk: The workflow depends on a local age-compatible encryption tool being available. <br>
Mitigation: Install and verify age on the target device before use; do not downgrade to unauthenticated ZIP passwords, plain archives, or custom encryption. <br>


## Reference(s): <br>
- [WorkBuddy 项目续接 Skill Page](https://clawhub.ai/taogeo/skills/workbuddy-workspace-relay) <br>
- [Agent 工作流](references/agent-workflow.md) <br>
- [WorkBuddy Workspace Relay package format](references/package-format.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Markdown, Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown handoff content, local shell commands, JSON command results, restored project files, and encrypted .wbpack files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated .wbpack files are confidential workspace handoff packages and should be protected with a strong password.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
