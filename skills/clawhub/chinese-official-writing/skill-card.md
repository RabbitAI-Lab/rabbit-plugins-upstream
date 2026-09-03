## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核；用户要求写申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、制度、规定、办法、管理办法、细则、操作规程、工作要点、总结、调研、讲话、致辞、可研、审查材料、AI 算力等正式文本，或需校验这类材料的文种、格式、去口语化、降 AI 味时使用；适用于机关、企事业单位、学校、新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and writers use this skill to draft, revise, compress, and review Chinese official documents, formal workplace materials, and news-style drafts. It helps check genre fit, official-document structure, formal tone, factual boundaries, anti-AI phrasing, and formatting considerations for government, enterprise, school, and newsroom contexts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated official text can still contain incorrect or unsupported facts, dates, authorities, signatures, policy sources, or approval conclusions if the user's inputs are incomplete.

Mitigation: Review generated text against the source materials and confirm all official elements through the user's organizational approval process before use.

Risk: Formal DOCX or GB/T 9704 formatting may not match a specific organization's required template.

Mitigation: Check final formatting against the applicable organizational template before distribution or filing.

## Reference(s):

- [AI 算力与技术服务材料](references/ai-compute-docs.md)
- [反 AI 表达检查](references/anti-ai-patterns.md)
- [论证链条](references/argument-chains.md)
- [联网搜索与公开来源核验](references/external-research.md)
- [总审层级](references/final-review-layers.md)
- [敬谦称谓和机关用语](references/formal-addressing.md)
- [GB/T 9704-2012 常用格式参考](references/format-gbt9704.md)
- [公文行文用语](references/formulaic-language.md)
- [文种清单](references/genre-checklist.md)
- [文种与专项 Playbook](references/genre-playbooks.md)
- [文种路由](references/genre-routing.md)
- [办理要素](references/handling-elements.md)
- [信息选择](references/information-selection.md)
- [公文语言风格](references/official-style.md)
- [AI 写稿轻量校对](references/proofreading-checklist.md)
- [复核清单](references/review-checklist.md)
- [任务路由卡](references/task-route-cards.md)
- [写作流程](references/workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Chinese formal prose, review notes, and Markdown or plain text depending on the user's requested delivery]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated text should preserve user-provided facts and flag or avoid unsupported official elements such as dates, authorities, signatures, policy sources, and approval conclusions.]

## Skill Version(s):

1.6.25 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
