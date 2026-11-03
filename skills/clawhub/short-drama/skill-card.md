## Description:

初始化和继续短剧项目，路由创作阶段，查看创作台并导出当前成果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

短剧创作者可用它初始化和管理本地项目、查看进度，并把任务路由到相应的创作阶段。它也可用于查看创作台和导出项目成果。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared dashboard link could expose access to a local project workspace.

Mitigation: Keep the dashboard link private and stop the dashboard with --stop when finished.

Risk: Exported project files may contain material the creator has not reviewed for sharing.

Mitigation: Review exported files before sharing them.

Risk: Companion skills are separate packages and have not been assessed by this skill's static artifact review.

Mitigation: Assess companion skills separately before installing them.

## Reference(s):

- [短剧创作路由 on ClawHub](https://clawhub.ai/worldwonderer/skills/short-drama)
- [Creator-first 工作流](artifact/references/creator-workflow.md)
- [创作文档](artifact/references/creator-documents.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON configuration, Shell commands, Project guidance]

**Output Format:** [Markdown project documents, JSON configuration, and concise text or shell-command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the requested project task; this router manages project files and stages and does not itself produce media.]

## Skill Version(s):

1.0.31 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
