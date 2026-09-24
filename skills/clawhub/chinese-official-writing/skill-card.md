## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩、润色、审校、文种核对、去口语化、降 AI 味及 Word 格式处理，适用于机关、企事业单位、学校和新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and organizational writing teams use this skill to draft, revise, compress, proofread, and review Chinese official documents, business materials, work reports, news copy, and related Word-format deliverables. It is intended for formal workplace writing where facts, document genre, tone, required elements, and formatting need close checking before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated official documents may contain incorrect or incomplete facts, dates, policy references, responsibility statements, or commitments.

Mitigation: Review all generated content against the user's source materials before formal use, with special attention to facts, figures, dates, policy bases, and commitments.

Risk: Confidential, prepublication, personal, or regulated draft materials could be exposed if used as search queries during external research.

Mitigation: Avoid sending sensitive draft details to web search; use sanitized queries or provide trusted source material directly.

Risk: Word-format or formal-document outputs may omit required local template, signing, seal, numbering, or filing details.

Mitigation: Check final formatting and formal issuance elements against the user's organization template and applicable procedures before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [README](artifact/README.md)
- [Reference index](artifact/references/reference-index.md)
- [Common writing and delivery rules](artifact/references/writing-rules.md)
- [Genre routing](artifact/references/genre-routing.md)
- [Review checklist](artifact/references/review-checklist.md)
- [Prose lint usage](artifact/references/prose-lint-usage.md)
- [Official document and Word formatting reference](artifact/references/format-gbt9704.md)
- [External research guidance](artifact/references/external-research.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Chinese prose drafts, revised text, review comments, checklists, and occasional Markdown or shell command snippets for local validation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Word-format handoff guidance when a host document tool is available; generated content requires human review before formal use.]

## Skill Version(s):

2.0.12 (source: ClawHub release metadata and README)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
