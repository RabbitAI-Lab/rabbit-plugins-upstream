## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩、润色、审校、文种核对、去口语化、降 AI 味及 Word 格式处理，适用于机关、企事业单位、学校和新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and document-focused agents use this skill to draft, revise, compress, proofread, and format Chinese official documents, transactional work materials, news copy, and related Word-ready text. It is aimed at official-document workflows for agencies, enterprises, institutions, schools, and news organizations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-assisted official documents may contain incorrect facts, dates, data, policy citations, commitments, confidentiality labels, or internal business details.

Mitigation: Review generated drafts carefully before formal use, with particular attention to facts, figures, sources, responsibilities, commitments, and sensitive information.

Risk: Helper scripts read draft files supplied by the user, and current-policy checks may involve web research.

Mitigation: Run helper scripts only on intended local drafts and avoid providing confidential or personal data unless the operating environment and review process are appropriate.

## Reference(s):

- [README](README.md)
- [Reference Index](references/reference-index.md)
- [Writing Rules](references/writing-rules.md)
- [Review Checklist](references/review-checklist.md)
- [GB/T 9704 Formatting Rules](references/format-gbt9704.md)
- [Prose Lint Usage](references/prose-lint-usage.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Chinese prose, review notes, Markdown when requested, and occasional shell commands for local draft checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May separate unresolved gaps, modification suggestions, or remaining questions into a postscript after the main draft.]

## Skill Version(s):

2.0.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
