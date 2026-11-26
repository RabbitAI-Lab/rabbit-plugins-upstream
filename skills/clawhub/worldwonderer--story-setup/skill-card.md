## Description:

为 Claude Code、OpenCode、Codex、Google Antigravity、ZCode、OpenClaw、Reasonix 及通用 Agent 部署并检查网文写作工具集。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

网文作者和开发者用它在支持的 AI 编码宿主或通用 Agent 项目中部署、更新或诊断写作工具集，并配置写作规则、子代理和项目钩子。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan flags shell-interpolated URL behavior as a review risk.

Mitigation: Review this behavior and its input handling before enabling it; avoid it if it is not needed.

Risk: Browser research and writing-enforcement behavior may extend beyond setup needs, and scanning coverage is incomplete.

Mitigation: Decide whether these features are needed before installation and review the remaining behavior; scanning fully inspected 118 of 135 components, with several checks degraded.

Risk: Installer instructions have not been verified by the security assessment.

Mitigation: Check installer commands against trusted project documentation before running them.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/worldwonderer/skills/story-setup)
- [Project reference (GitHub)](https://github.com/zenstory-ai/oh-story-claudecode)
- [Diagnostics guide](references/diagnostics.md)
- [Codex deployment guide](references/deploy-codex.md)
- [Claude Code deployment guide](references/deploy-claude-code.md)
- [OpenCode deployment guide](references/deploy-opencode.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance, shell commands, and project configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Host-specific setup and diagnostic results; may add or update project files while preserving user configuration.]

## Skill Version(s):

1.2.26 (source: ClawHub release metadata; packaged SKILL.md reports 1.3.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
