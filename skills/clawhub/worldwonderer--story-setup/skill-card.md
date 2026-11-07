## Description:

网文写作工具集基础设施部署与检查，支持多个 CLI 宿主及通用 Agent 的项目配置。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

面向网文作者及维护写作项目的开发者，用于在支持的 CLI 或通用 Agent 项目中部署、更新并检查写作工具集配置。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser commands can execute commands embedded in links.

Mitigation: Wait for the browser URL handling fix before enabling those paths, and use a dedicated research browser tab.

Risk: An installer can delete an existing backup.

Mitigation: Wait for the Antigravity backup cleanup fix and back up the writing project before deployment.

Risk: Searches may expose confidential story details.

Mitigation: Do not include confidential story details in searches.

Risk: Installed hooks and separately referenced OpenClaw companion skills need review; the complete suite was not validated end to end.

Mitigation: Review installed hooks and review the companion skills separately before use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/worldwonderer/skills/story-setup)
- [Project link listed in skill metadata](https://github.com/zenstory-ai/oh-story-claudecode)

## Skill Output:

**Output Type(s):** [Configuration, Files, Shell commands, Markdown guidance, Deployment report]

**Output Format:** [Project configuration files and concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deployment results depend on the selected host and project layout.]

## Skill Version(s):

1.2.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
