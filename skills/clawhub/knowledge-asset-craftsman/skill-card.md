## Description:

把问答库、逐字稿、会议记录、培训材料、长文章、课程文档、制度文件、操作手册等原始资料，转成可追溯、可检索、可更新、适合 RAG 和问答智能体使用的结构化知识资产。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jeasonhaitao](https://clawhub.ai/user/jeasonhaitao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, knowledge-base maintainers, and agent builders use this skill to convert user-provided source documents into traceable JSONL knowledge assets with a generated Markdown review view for RAG and question-answering workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected source documents may contain confidential or personal data that would be carried into generated knowledge assets.

Mitigation: Review and redact sensitive inputs before processing, and keep generated JSONL, Markdown, manifests, and reports in approved destinations.

Risk: Incorrect source interpretation can produce misleading knowledge entries for downstream RAG or question-answering systems.

Mitigation: Use the generated Markdown review view, quality report, source spans, and conflict or pending-review statuses before publishing assets downstream.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jeasonhaitao/skills/knowledge-asset-craftsman)
- [Knowledge schema reference](references/knowledge-schema.md)
- [Conversation semantic splitting guide](references/conv-semantic-splitting.md)
- [Tag generation rules](references/tag-rules.md)
- [Knowledge block template](assets/knowledge-block-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [JSONL primary data, generated Markdown review view, manifests, dictionaries, evaluation records, quality reports, and concise downstream handoff guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSONL as the single source of truth and treats Markdown as a generated human-review view.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
