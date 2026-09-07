## Description:

增强 Agent 的本地屏幕控制能力，利用本地屏幕视觉技术提高界面识别与定位效率，并通过自然语言创建和维护自动化流程。配合支持 Windows 与 macOS 的“屏幕自动化小助手”完成流程的安装、升级、修复、卸载、运行和结果读取。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaozs-com](https://clawhub.ai/user/xiaozs-com)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to let an agent safely inspect and operate local desktop windows through the Screen Automation Helper, or to create reusable screen automation workflows for repeated tasks. It is suited for Windows and macOS workflows that need visible target confirmation, local screen recognition, controlled clicks, typing, clipboard actions, validation, and result reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enable broad local screen-control actions, including reading visible screen content, selecting windows, clicking, typing, clipboard use, and workflow management.

Mitigation: Install and enable it only when those capabilities are intended, require visible target confirmation before actions, and review each workflow's permissions before deployment.

Risk: Automating sensitive approvals, payments, public posting, deletions, account authorization, or similar high-impact actions could cause unintended user harm.

Mitigation: Do not allow workflows to perform those actions; stop for user review when a task enters a sensitive approval or authorization boundary.

Risk: Screen recognition or coordinate targeting can be wrong when the target window changes, is obscured, or has ambiguous UI elements.

Mitigation: Use the skill's observe-operate-verify pattern, bind actions to a confirmed target window, re-observe after each UI-changing action, and stop when the target is not unique or the result cannot be verified.

Risk: Reusable workflow packages may drift from the actual application UI or include unsafe permissions or code extensions.

Mitigation: Run inspect and validate before installation, keep first real runs supervised, require bounded loops and explicit stop conditions, and use workflow.py only for complex cases that cannot be expressed in workflow.md.

## Reference(s):

- [Workflow Standard](references/workflow-standard.md)
- [Screen Automation Helper homepage](https://www.xiaozs.com/sah/)
- [Source repository](https://github.com/xiaozs-com/screen-automation-engineer)
- [ClawHub skill page](https://clawhub.ai/xiaozs-com/skills/screen-automation-engineer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, reusable workflow files, and structured result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce workflow.md packages and optional workflow.py extensions when a repeated automation task requires them.]

## Skill Version(s):

0.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
