## Description:

网文写作工具集基础设施部署与检查。为 Claude Code / OpenCode / Codex / Google Antigravity / ZCode / OpenClaw / Reasonix 提供内置适配；Web AI / 通用 Agent 可走 skills + AGENTS.md 文件模式。触发方式：/story-setup、$story-setup、「准备写书」「帮我搭一下环境」「配置写作项目」「检查写作环境」。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

面向使用 AI 编程助手的网文作者和项目维护者，用于部署、检查或修复写作项目所需的智能体配置、助手和钩子。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan flags an unescaped URL-to-shell command risk and risky installation guidance.

Mitigation: Review install commands and their sources before running them; prefer pinned, verified installers.

Risk: Setup may delete existing backup data.

Mitigation: Back up the project separately and review cleanup targets before deployment.

Risk: Installed hooks may inspect or restrict manuscript operations.

Mitigation: Review hook registrations and scope before enabling them.

## Reference(s):

- [ClawHub release](https://clawhub.ai/worldwonderer/skills/story-setup)
- [Project link listed in skill metadata](https://github.com/zenstory-ai/oh-story-claudecode)

## Skill Output:

**Output Type(s):** [Configuration files, Code, Shell commands, Guidance]

**Output Format:** [Project configuration and support files, with Markdown guidance and a deployment report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates host-specific writing-agent setup files and reports deployment checks.]

## Skill Version(s):

1.2.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
