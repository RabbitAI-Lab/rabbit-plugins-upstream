## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核，并帮助校验文种、格式、语气和去口语化问题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees and external users use this skill to draft, revise, compress, and review Chinese official documents, work materials, institutional rules, news releases, speeches, summaries, feasibility materials, and AI-compute-related formal texts. It is intended for agencies, enterprises, public institutions, schools, and news organizations that need formal Chinese writing support grounded in supplied materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional DOCX linter should not be used on untrusted documents without resource isolation.

Mitigation: Use the linter only with trusted documents, or run it in a constrained environment when checking outside DOCX files.

Risk: Optional external hooks and paid or pro links are outside the automatic skill install inspected by the security evidence.

Mitigation: Review those external components separately before enabling or relying on them.

Risk: Formal drafts can mislead readers if unsupported facts, dates, amounts, policy claims, or conclusions are accepted without review.

Mitigation: Review generated drafts against the supplied materials and confirm external or time-sensitive facts before official use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [README](README.md)
- [Reference Index](references/reference-index.md)
- [Genre Routing](references/genre-routing.md)
- [GB/T 9704 Formatting](references/format-gbt9704.md)
- [Review Checklist](references/review-checklist.md)
- [Prose Lint Usage](references/prose-lint-usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain text or Markdown guidance with optional shell commands for local prose linting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce formal document drafts, revised text, compression results, review notes, formatting guidance, and optional linter commands; DOCX handling requires a separate document tool.]

## Skill Version(s):

1.6.36 (source: evidence release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
