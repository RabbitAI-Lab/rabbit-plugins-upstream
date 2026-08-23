## Description:

DeepSeek Harness（dsh）傻瓜式本地启动助手，引导用户获取 DeepSeek API Key，按 macOS、Windows 或 Linux 环境配置 Node.js、npm 镜像、dsh 安装、Web 服务启动和桌面快捷方式。

This skill is ready for commercial/non-commercial use.

## Publisher:

[onsoul](https://clawhub.ai/user/onsoul)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to understand, install, configure, and launch DeepSeek Harness locally with a desktop shortcut and local Web UI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install local software, change npm registry settings, and create a persistent desktop launcher.

Mitigation: Ask the agent for a dry-run summary of the exact commands before execution and approve only the environment changes you want.

Risk: A global dsh installation and desktop shortcut may persist after the session.

Mitigation: Use the documented npx launch option when you do not want a global install or persistent launcher.

Risk: DeepSeek API keys are required for model access.

Mitigation: Keep API keys in local settings or environment variables and do not include them in shared files, logs, or responses.

## Reference(s):

- [DeepSeek Harness GitHub repository](https://github.com/deepseek-ai/deepseek-harness)
- [DeepSeek Platform](https://platform.deepseek.com)
- [ClawHub skill page](https://clawhub.ai/onsoul/skills/fore-vip-ds-harness)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell, PowerShell, batch, and desktop-entry code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate local launch scripts or shortcuts during agent execution.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
