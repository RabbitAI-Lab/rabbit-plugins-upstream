## Description:

创建或继续本地短剧与漫剧项目，衔接创作环节，管理全局配置、制作形态与视觉风格，并提供本地创作台和交付打包。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

短剧创作者与制作团队可用此技能初始化或继续本地项目、调整全局制作配置、选择制作形态、查看创作进度，并整理和打包每集的制作资料。具体剧本、设定、提示词、分镜、剪辑与审查工作可交由对应创作技能完成。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The benign security verdict has medium confidence and partial coverage: 24 of 26 components were inspected, two partly inspected, with bounded static analysis and some referenced paths missing.

Mitigation: Review the skill source and requested host file, network, and shell access before installation; limit access to what the project tasks require.

Risk: The scan summary notes an undeclared tool scope.

Mitigation: Check the host's effective tool permissions and keep them limited to the operations needed for the requested task.

## Reference(s):

- [五份创作文档](references/creator-documents.md)
- [制作形态与视觉风格](references/production-form-profiles.md)
- [规则与路由索引](references/knowhow-index.md)
- [短剧创作 ClawHub release](https://clawhub.ai/worldwonderer/skills/short-drama)
- [Publisher profile: worldwonderer](https://clawhub.ai/user/worldwonderer)

## Skill Output:

**Output Type(s):** [Markdown, JSON configuration, Shell commands, Project files]

**Output Format:** [Markdown creator documents, JSON project configuration and delivery manifests, and shell commands or guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the requested project task; production media generation is handled by companion skills.]

## Skill Version(s):

1.0.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
