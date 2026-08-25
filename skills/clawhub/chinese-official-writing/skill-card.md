## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核；用户要求写申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、制度、规定、办法、管理办法、细则、操作规程、工作要点、总结、调研、讲话、致辞、可研、审查材料、AI 算力等正式文本，或需校验这类材料的文种、格式、去口语化、降 AI 味时使用；适用于机关、企事业单位、学校、新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees and external users working in Chinese-language institutional, enterprise, school, media, or government-adjacent contexts use this skill to draft, revise, condense, and review formal documents, official correspondence, news releases, reports, requests, rules, summaries, feasibility materials, and related work texts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive or official documents may contain facts, approvals, dates, seals, Word formatting, or institutional requirements that the skill cannot verify on its own.

Mitigation: Manually review sensitive or official drafts before submission, especially where public-source verification, Word formatting, seals, dates, or institutional approvals are involved.

Risk: The optional local prose lint script can surface language, formatting, and repetition warnings, but it does not replace document-type or source-material review.

Mitigation: Treat lint findings as advisory and review final text against the governing document type, user-provided facts, and applicable institutional requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [Workflow](references/workflow.md)
- [Genre Routing](references/genre-routing.md)
- [Handling Elements](references/handling-elements.md)
- [Information Selection](references/information-selection.md)
- [Official Style](references/official-style.md)
- [Review Checklist](references/review-checklist.md)
- [GB/T 9704 Format Guidance](references/format-gbt9704.md)
- [External Research](references/external-research.md)
- [AI Compute Documents](references/ai-compute-docs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown prose, with optional shell commands for local prose linting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can produce Chinese formal-document drafts, revised text, review findings, formatting guidance, and optional lint command suggestions.]

## Skill Version(s):

1.6.16 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
