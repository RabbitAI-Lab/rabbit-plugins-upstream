## Description:

将已写好的小说反向解析并整理为可续写的写作项目，按篇幅选择长篇或短篇迁移流程。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

面向希望把半成品或完本小说整理成可续写工程的作者，用于分析原文并迁移设定、大纲、正文和长篇追踪资料。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may archive prior analysis outputs or replace outline files during a retry.

Mitigation: Confirm the project paths and import scope before running; keep backups of existing materials and review generated files.

Risk: Security review coverage is incomplete: one component was only partially inspected and one reference was missing.

Mitigation: Review the partially inspected component and resolve the missing reference before relying on the scan assessment.

## Reference(s):

- [Length routing](references/length-routing.md)
- [Deep analysis workflow](references/deep-analysis.md)
- [Long-form structure mapping](references/structure-mapping-long.md)
- [Short-form structure mapping](references/structure-mapping-short.md)
- [Outline reversal workflow](references/outline-reverse.md)
- [Tracking initialization](references/import-tracking.md)
- [Import completion report](references/import-report.md)
- [Project link declared in skill metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-import)

## Skill Output:

**Output Type(s):** [Markdown files, Configuration files, Guidance]

**Output Format:** [A structured writing-project directory containing Markdown documents and JSON tracking state]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project structure varies by long-form or short-form input; long-form imports include chapter outlines and tracking files.]

## Skill Version(s):

1.0.43 (source: target release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
