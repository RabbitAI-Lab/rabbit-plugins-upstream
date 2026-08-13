## Description:

创建、修改、排查、调试和打包希沃白板 EasiNote 5 原生插件的开发指南。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lindexi](https://clawhub.ai/user/lindexi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build, modify, debug, and package EasiNote 5 native .NET 6/WPF plugins. It provides task-scoped guidance for project setup, lifecycle handling, host UI extensions, WPF integration, safe restarts, and packaging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated plugin guidance can affect the EasiNote host UI and document state.

Mitigation: Use the skill only for EasiNote native plugin work, keep UseEasiNote at the minimum level that compiles, and validate behavior against the target EasiNote version.

Risk: Restart or exit flows can interrupt user work or create duplicate host instances if used without confirmation.

Mitigation: Require explicit user confirmation, reuse the complete host exit flow, and distinguish user cancellation from restart failures.

Risk: Telemetry, package contents, or command-line arguments can expose sensitive data.

Mitigation: Exclude credentials, tokens, personal data,课件内容, internal addresses, and local machine paths from telemetry and packaged artifacts.

## Reference(s):

- [项目搭建与调试配置](references/project-setup.md)
- [生命周期、进程形态与容器就绪](references/lifecycle-and-container.md)
- [常用 API 配方](references/api-recipes.md)
- [HeadToolBarItem 与“学科工具”入口](references/head-toolbar-and-subject-tools.md)
- [WPF 视觉接入](references/wpf-visual-integration.md)
- [安全退出与重启 EasiNote](references/safe-host-restart.md)
- [完整开发示例](references/complete-examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with C#, XML, JSON, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-scoped guidance for Windows, .NET 6, WPF, and EasiNote 5 native plugin development.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
