## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩、润色、审校、文种核对、去口语化、降 AI 味及 Word 格式处理，适用于机关、企事业单位、学校和新闻机构。涵盖申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、制度、规定、办法、细则、操作规程、工作要点、总结、调研、讲话、致辞、主持词、述职、可研、审查材料、技术需求、新闻消息、编者按、新闻评论，以及采购、整改、反馈和 AI 算力等场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and developers can use this skill to draft, revise, shorten, polish, review, and format Chinese official documents, work materials, news copy, and related Word-ready text. It is most useful when the user provides source facts, a draft, a document purpose, or a required genre.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential or sensitive draft details could be exposed if optional web research is used for a private document.

Mitigation: For confidential drafts, instruct the agent not to search the web or share document details externally.

Risk: Generated official-document text or Word-formatted output may contain factual, policy, formatting, or issuance errors.

Mitigation: Review generated copy, Word files, and any formal issuance language before use.

Risk: The skill can rely on host document tools and local checking scripts, so tool availability may affect final formatting and checks.

Mitigation: Use the local checks where available and record any checks that could not be completed before relying on the draft.

## Reference(s):

- [README](README.md)
- [Reference Index](references/reference-index.md)
- [Common Writing and Delivery Rules](references/writing-rules.md)
- [Review Checklist](references/review-checklist.md)
- [Prose Lint Usage](references/prose-lint-usage.md)
- [GB/T 9704 Format Rules](references/format-gbt9704.md)
- [External Research Rules](references/external-research.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, guidance]

**Output Format:** [Plain text or Markdown drafts, review notes, Word-ready content, and occasional shell commands for local draft checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include post-draft notes for missing facts, unresolved issues, or checks that need human review.]

## Skill Version(s):

2.0.3 (source: server release metadata and README)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
