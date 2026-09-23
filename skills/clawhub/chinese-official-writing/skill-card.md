## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩、润色、审校、文种核对、去口语化、降 AI 味及 Word 格式处理，适用于机关、企事业单位、学校和新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, writers, reviewers, and document-support teams use this skill to draft, revise, compress, proofread, and review Chinese official documents, work materials, news items, and related Word-format body text. It is intended for workflows where user-provided facts, templates, latest drafts, scope limits, and formal document requirements must be preserved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential government, school, enterprise, procurement, personnel, or policy drafts may contain sensitive material.

Mitigation: Keep web research off unless it is needed, and when research is required search only high-level public terms without including sensitive draft text.

Risk: AI-assisted official documents may contain errors, omissions, unsupported facts, or incorrect policy and data references.

Mitigation: Require human review before formal use, with special attention to facts, figures, citations, policy basis, responsibilities, and commitments.

Risk: Formal document fields such as document numbers, seals, signers, dates, and official formatting details may be missing from the source material.

Mitigation: Do not invent formal issuance elements; preserve provided templates and list unresolved required fields for confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [README](README.md)
- [Reference index](references/reference-index.md)
- [Writing rules](references/writing-rules.md)
- [Review checklist](references/review-checklist.md)
- [GB/T 9704 and Word formatting reference](references/format-gbt9704.md)
- [Prose lint usage](references/prose-lint-usage.md)
- [External research and public-source verification](references/external-research.md)
- [Source repository listed in README](https://github.com/gongyu0918-debug/chinese-official-writing-skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Chinese prose, review notes, and optional Markdown or plain-text document content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use bounded Python helper scripts for draft length measurement, prose scanning, exact-text comparison, and replacement-scope checks; Word output depends on host document tooling.]

## Skill Version(s):

2.0.11 (source: server release metadata and README)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
