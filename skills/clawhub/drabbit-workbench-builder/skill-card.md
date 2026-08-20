## Description:

通过 5-7 个问题了解用户职业、工作需求和手机型号，并生成个性化单页 PWA 工作台，覆盖任务、日程、记账、项目模块、桌面添加和可选多端同步。

This skill is ready for commercial/non-commercial use.

## Publisher:

[drabbit777](https://clawhub.ai/user/drabbit777)

### License/Terms of Use:

MIT

## Use Case:

Agents use this skill with end users who want a personalized mobile and desktop workbench. It guides the agent through interviewing the user, customizing a static PWA template, deploying it, and giving device-specific installation and sync setup guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated workbenches can sync personal work, finance, and image data to CloudBase with weakly scoped anonymous access and incomplete privacy controls.

Mitigation: Review CloudBase environment IDs, anonymous-login settings, database rules, and uploaded fields before enabling sync; avoid sensitive finance, account, student, client, or confidential work data unless rules are hardened.

Risk: Users may treat the generated hosted PWA as private even when sync and hosting settings have not been reviewed.

Mitigation: Tell users what data may be stored locally or uploaded, verify what the deployed app sends to CloudBase, and keep photo sync disabled or stripped unless storage rules are explicit.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drabbit777/skills/drabbit-workbench-builder)
- [Customization parameters](references/customization-params.md)
- [Template structure](references/template-structure.md)
- [Bugs and fixes](references/bugs-and-fixes.md)
- [Tencent CloudBase console](https://console.cloud.tencent.com/tcb)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets, configuration steps, shell commands, and generated PWA files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a customized static PWA workspace template and setup instructions; optional CloudBase sync can store user workbench data when enabled.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
