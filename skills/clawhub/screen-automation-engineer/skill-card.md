## Description:

增强 Agent 的屏幕理解和控制能力，利用本地屏幕视觉技术提高界面识别与定位效率，并通过自然语言创建和维护自动化流程。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaozs-com](https://clawhub.ai/user/xiaozs-com)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent perform supervised screen tasks through the Xiaozs Screen Automation Helper, then turn repeated tasks into maintainable workflows when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables an agent to control the user's screen through a local helper app.

Mitigation: Review workflows before first run, supervise installs and irreversible actions, confirm the target window, and stop when the result cannot be verified.

Risk: Screen observations or screenshots may expose sensitive information when vision-model assistance is used.

Mitigation: Confirm the provider, authorized screen region, and purpose before sending screenshots, and keep passwords, verification codes, keys, and unrelated private content out of model inputs, logs, and workflows.

## Reference(s):

- [Screen Automation Helper](https://www.xiaozs.com/sah/)
- [ClawHub skill page](https://clawhub.ai/xiaozs-com/skills/screen-automation-engineer)
- [Agent Bridge and Vision Model Standard](artifact/references/agent-bridge.md)
- [Workflow Development Standard](artifact/references/workflow-standard.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and workflow files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include platform-specific PowerShell or bash commands and workflow package content.]

## Skill Version(s):

1.1.28 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
