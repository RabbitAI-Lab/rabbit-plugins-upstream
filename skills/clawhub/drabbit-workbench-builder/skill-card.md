## Description:

个人工作台搭建器通过 5-7 个问题了解用户的职业、工作需求和手机型号，生成个性化单页 PWA 工作台并部署到 CloudStudio，支持任务、日程、记账、项目等模块。

This skill is ready for commercial/non-commercial use.

## Publisher:

[drabbit777](https://clawhub.ai/user/drabbit777)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to interview a user, customize a personal workbench PWA from the bundled template, deploy it to CloudStudio, and provide device-specific setup guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generated workbench can include personal profile, work, task, calendar, finance, student, client, or credential-related text in a hosted CloudStudio app or optional CloudBase sync.

Mitigation: Review data before deployment, avoid sensitive content unless the user accepts the storage risk, and configure CloudBase access rules carefully.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drabbit777/skills/drabbit-workbench-builder)
- [Customization Parameters](references/customization-params.md)
- [Template Structure](references/template-structure.md)
- [Bugs and Fixes](references/bugs-and-fixes.md)
- [CloudBase Console](https://console.cloud.tencent.com/tcb)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code, shell commands, configuration edits, and generated PWA files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce customized HTML, service worker, CloudBase sync configuration, PWA icon assets, deployment commands, and device-specific installation instructions.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
