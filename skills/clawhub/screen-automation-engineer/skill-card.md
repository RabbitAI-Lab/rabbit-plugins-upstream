## Description:

增强 Agent 的本地屏幕控制能力，利用本地屏幕视觉技术提高界面识别与定位效率，并通过自然语言创建和维护自动化流程。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaozs-com](https://clawhub.ai/user/xiaozs-com)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect selected desktop windows, perform confirmed screen actions, and create maintainable automation workflows through the Screen Automation Helper companion app.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can observe selected windows and perform confirmed mouse, keyboard, clipboard, and workflow actions through a local helper.

Mitigation: Install only in approved environments, confirm target windows and workflow permissions, and supervise first runs before using repeatable workflows.

Risk: Ambiguous UI state or an incorrect target window could lead to unintended desktop actions.

Mitigation: Use the documented target confirmation, observe-then-act checks, success criteria, and stop conditions before changing the interface.

## Reference(s):

- [Server-resolved source repository](https://github.com/xiaozs-com/screen-automation-engineer)
- [ClawHub skill page](https://clawhub.ai/xiaozs-com/skills/screen-automation-engineer)
- [Screen Automation Helper homepage](https://www.xiaozs.com/sah/)
- [Workflow development standard](artifact/references/workflow-standard.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and workflow files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce workflow.md packages with optional workflow.py for repeatable screen automation; execution depends on the local companion helper.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
