## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核；用户要求写申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、制度、规定、办法、管理办法、细则、操作规程、工作要点、总结、调研、讲话、致辞、可研、审查材料、AI 算力等正式文本，或需校验这类材料的文种、格式、去口语化、降 AI 味时使用；适用于机关、企事业单位、学校、新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and document-focused teams use this skill to draft, revise, condense, and review Chinese official documents, workplace materials, news items, institutional rules, reports, speeches, and related formal text. It is intended to keep drafts grounded in user-provided facts while supporting document-genre routing, tone cleanup, format checks, and review suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Official-document and business drafts may contain sensitive organizational facts.

Mitigation: Treat drafts and source materials as sensitive, and share only the information needed for the task.

Risk: Generated text may be inaccurate, unsupported, or unsuitable for filing if the source material is incomplete.

Mitigation: Review generated text before filing and verify names, dates, amounts, approval language, and policy references against authoritative materials.

Risk: The optional local prose-lint script processes user-supplied files.

Mitigation: Run the lint script only on trusted, normal-sized files that are expected to contain text for document review.

Risk: Optional external Hook and Pro links are outside the bundled ClawHub release.

Mitigation: Evaluate those external components separately before enabling or purchasing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [README](README.md)
- [Writing workflow](references/workflow.md)
- [Genre routing](references/genre-routing.md)
- [Genre and special-purpose playbooks](references/genre-playbooks.md)
- [Handling elements](references/handling-elements.md)
- [Information selection](references/information-selection.md)
- [Official style](references/official-style.md)
- [Formulaic language](references/formulaic-language.md)
- [GB/T 9704-2012 formatting reference](references/format-gbt9704.md)
- [Review checklist](references/review-checklist.md)
- [Final review layers](references/final-review-layers.md)
- [Anti-AI expression checks](references/anti-ai-patterns.md)
- [AI compute and technical service materials](references/ai-compute-docs.md)
- [External source verification](references/external-research.md)
- [Optional hook usage](https://github.com/gongyu0918-debug/chinese-official-writing-skill/blob/main/chinese-official-writing/hooks/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands, configuration]

**Output Format:** [Markdown or plain Chinese formal-document prose, with optional review notes, checklists, and command snippets when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve user-provided facts, avoid unresolved placeholders in final drafts, and distinguish drafting from review-only tasks.]

## Skill Version(s):

1.6.30 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
