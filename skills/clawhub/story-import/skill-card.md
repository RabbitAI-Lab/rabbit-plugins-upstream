## Description:

逆向导入已有小说。将已写好的小说（半成品或完本）反向解析为标准项目目录结构，兼容 story-long-write / story-short-write 后续写作流程；内部复用 story-long-analyze / story-short-analyze 的拆解管道，按篇幅自动分流。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

小说作者将已有的半成品或完本作品整理成可续写的项目，供后续长篇或短篇写作流程继续使用。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Existing project files, especially tracking notes, may not be fully preserved by the migration archive.

Mitigation: Back up the existing project and tracking notes before importing.

Risk: Strict chapter validation may reject some manuscript imports.

Mitigation: Review validation feedback and chapter boundaries, then correct the source or import scope as needed.

Risk: The configured AI host may analyze manuscript content during import.

Mitigation: Use manuscripts you are comfortable having your configured AI host analyze.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-import)
- [Project link listed in skill metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Deep analysis workflow](artifact/references/deep-analysis.md)
- [Long-form structure mapping](artifact/references/structure-mapping-long.md)
- [Short-form structure mapping](artifact/references/structure-mapping-short.md)
- [Tracking initialization](artifact/references/import-tracking.md)
- [Import completion report](artifact/references/import-report.md)

## Skill Output:

**Output Type(s):** [Files, Markdown, JSON, Guidance]

**Output Format:** [Novel project files in Markdown and JSON, plus a concise completion report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project structure and files vary with manuscript length and import scope.]

## Skill Version(s):

1.0.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
