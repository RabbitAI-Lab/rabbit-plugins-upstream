## Description:

Drafts, revises, compresses, proofreads, reviews, and formats Chinese official documents, workplace materials, and news drafts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees and external users use this skill to prepare and review Chinese official documents, workplace materials, and formal news writing from supplied facts, drafts, templates, and revision requirements. It supports drafting, rewriting, compression, tone cleanup, document-genre checks, review comments, and Word-oriented body formatting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Very large or crafted DOCX, TXT, or Markdown inputs could cause bundled local checking scripts to hang or exhaust resources.

Mitigation: Run document checks in a host environment with CPU and memory limits, and avoid processing untrusted or unusually large files.

Risk: Generated official or workplace documents can contain incorrect facts, dates, amounts, responsibilities, or unsupported policy claims if source materials are incomplete.

Mitigation: Review drafts against the user's supplied materials and keep unresolved gaps or assumptions separate from the document body.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [README](README.md)
- [Skill instructions](SKILL.md)
- [Reference index](references/reference-index.md)
- [Writing rules](references/writing-rules.md)
- [Review checklist](references/review-checklist.md)
- [GB/T 9704 formatting](references/format-gbt9704.md)
- [Prose lint usage](references/prose-lint-usage.md)
- [AI compute scenario guidance](references/ai-compute-docs.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Plain text or Markdown, with optional generated document content, review comments, and local check commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use bundled Python helpers for draft length checks and prose linting when the task requires them.]

## Skill Version(s):

2.0.1 (source: release evidence, README.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
