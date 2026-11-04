## Description:

基于文件系统初始化和继续短剧或漫剧项目，提供 creator-first 五文档路由、本地 Dashboard、制作形态与 Look Development 决策。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

面向短剧与漫剧创作者，用于初始化和继续项目、路由创作阶段、查看项目进度与下一步、处理 Look Development，并导出当前创作资料。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The background dashboard can expose an access token that lets other local users read and edit project files.

Mitigation: Avoid the background dashboard until token logging is fixed, or restrict the .short-drama directory and existing log to your account before restarting with a fresh token. Choose a workspace containing only intended projects.

Risk: The companion skills used for individual creation stages were not covered by this static review.

Mitigation: Review and scan companion skills separately before using them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/worldwonderer/skills/short-drama)
- [Creator workflow](artifact/references/creator-workflow.md)
- [Runtime preflight](artifact/references/runtime-preflight.md)

## Skill Output:

**Output Type(s):** [Markdown, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown project documents, JSON configuration, and command-line guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and updates local project files and can display project status in a local dashboard.]

## Skill Version(s):

1.0.33 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
