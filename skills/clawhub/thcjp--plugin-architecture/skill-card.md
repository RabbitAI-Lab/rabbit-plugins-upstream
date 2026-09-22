## Description:

为 SkillHub 安装 UI 插件架构支持，使插件能够在 Control 仪表板侧边栏注册自定义视图和导航标签。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and SkillHub administrators use this skill to add plugin UI registration support and guide plugins in registering Control dashboard views, navigation groups, icons, and ordering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks an agent for broad file and command authority to install or alter SkillHub UI behavior.

Mitigation: Use it only in a disposable or version-controlled SkillHub environment and require the agent to show exact files and commands before making changes.

Risk: The installation materials and data-flow details are inconsistent or incomplete.

Mitigation: Review the missing installation materials and expected data flows before installing, and do not provide API keys or credentials until that review is complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/plugin-architecture)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [SkillHub skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with TypeScript examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Manual installation guidance should be reviewed before execution in a SkillHub environment.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
