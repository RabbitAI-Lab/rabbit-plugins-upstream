## Description:

逆向导入已有小说，将已写好的小说反向解析为标准项目目录结构，兼容后续长篇或短篇写作流程，并按篇幅选择相应拆解流程。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

面向希望继续创作已有小说的作者，分析其现有正文并整理成可续写的项目结构，包括设定、剧情大纲、章节资料和必要的长篇追踪信息。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broad “import” activation phrase may trigger the workflow in unrelated conversations.

Mitigation: Review the activation phrases before enabling the skill, and invoke /story-import explicitly when you want to start an import.

Risk: The security analysis had medium confidence and could not fully inspect the tracking script.

Mitigation: Review the tracking behavior before installation or use.

## Reference(s):

- [深度分析流程](artifact/references/deep-analysis.md)
- [长篇结构迁移](artifact/references/structure-mapping-long.md)
- [短篇结构迁移](artifact/references/structure-mapping-short.md)
- [细纲反推流程](artifact/references/outline-reverse.md)
- [细纲反推规则](artifact/references/outline-reverse-rules.md)
- [长篇追踪初始化](artifact/references/import-tracking.md)
- [导入报告与激活](artifact/references/import-report.md)
- [Repository link in skill metadata](https://github.com/zenstory-ai/oh-story-claudecode)

## Skill Output:

**Output Type(s):** [Markdown, Structured project files, Guidance]

**Output Format:** [Markdown project documents and structured tracking data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Files are organized into a project directory with layouts suited to long or short works.]

## Skill Version(s):

1.0.54 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
