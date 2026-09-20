## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩、润色、审校、文种核对、去口语化、降 AI 味及 Word 格式处理，适用于机关、企事业单位、学校和新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees and external users preparing Chinese official documents, work materials, news drafts, and formal review comments use this skill to draft, revise, compress, polish, audit, and format text while preserving user-provided facts and unresolved items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential government, school, enterprise, procurement, or internal drafts may expose sensitive details if optional online fact-checking is used without controls.

Mitigation: Use the skill without network access for confidential drafts unless a targeted public-source lookup is explicitly approved, and strip private names, unpublished facts, and sensitive document text from search terms.

Risk: Formal documents can contain incorrect facts, unresolved fields, or unsuitable document-type choices if source materials are incomplete.

Mitigation: Review generated drafts against the latest user-provided materials, preserve unresolved states, and keep missing items or follow-up questions in a separate after-text note.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [README](README.md)
- [Reference index](references/reference-index.md)
- [Writing rules](references/writing-rules.md)
- [Review checklist](references/review-checklist.md)
- [GB/T 9704 formatting](references/format-gbt9704.md)
- [Prose lint usage](references/prose-lint-usage.md)
- [External research rules](references/external-research.md)
- [AI compute scenario rules](references/ai-compute-docs.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Chinese prose, review notes, or Markdown when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a separate after-text note for missing information, modification suggestions, or unresolved issues; Word formatting depends on host document tools.]

## Skill Version(s):

2.0.7 (source: server release metadata and README)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
