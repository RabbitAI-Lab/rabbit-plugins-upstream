## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核；用户要求写申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、制度、规定、办法、管理办法、细则、操作规程、工作要点、总结、调研、讲话、致辞、可研、审查材料、AI 算力等正式文本，或需校验这类材料的文种、格式、去口语化、降 AI 味时使用；适用于机关、企事业单位、学校、新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and writing-support agents use this skill to draft, revise, compress, proofread, and format Chinese official documents, workplace materials, news copy, institutional rules, summaries, speeches, feasibility-review materials, and AI compute-related formal documents. It helps preserve document type, hierarchy, tone, factual boundaries, and required official-document elements while producing concise Chinese prose or review guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated official or formal documents may contain incorrect facts, unsupported implications, or wording that appears to imply authority, approval, seals, or final decisions.

Mitigation: Review the output manually against source materials, approval records, and organizational requirements before use or submission.

Risk: The optional local linter processes user-supplied TXT, Markdown, or DOCX drafts and may be unsuitable for unknown, untrusted, or very large files.

Mitigation: Run the linter only on trusted, reasonably sized files and treat its findings as drafting signals rather than final validation.

Risk: Time-sensitive policies, public-source facts, dates, amounts, contacts, document numbers, and institutional claims may be missing or outdated in the provided materials.

Mitigation: Verify current facts from authoritative sources when the task depends on them, and do not add unsourced specifics to final text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [README](README.md)
- [Reference index](references/reference-index.md)
- [Writing workflow](references/workflow.md)
- [Document type routing](references/genre-routing.md)
- [Information selection](references/information-selection.md)
- [GB/T 9704-2012 format reference](references/format-gbt9704.md)
- [Review checklist](references/review-checklist.md)
- [AI-pattern language review](references/anti-ai-patterns.md)
- [Optional prose linter usage](references/prose-lint-usage.md)
- [Optional hook usage](https://github.com/gongyu0918-debug/chinese-official-writing-skill/blob/main/chinese-official-writing/hooks/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Chinese prose drafts, revised document text, review notes, Markdown guidance, optional shell command snippets, and configuration guidance when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference an optional local prose linter for trusted, reasonably sized TXT, Markdown, or DOCX drafts; final official documents still require human review.]

## Skill Version(s):

1.6.35 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
