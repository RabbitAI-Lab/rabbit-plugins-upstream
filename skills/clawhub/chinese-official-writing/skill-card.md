## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核；用户要求写申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、制度、规定、办法、管理办法、细则、操作规程、工作要点、总结、调研、讲话、致辞、可研、审查材料、AI 算力等正式文本，或需校验这类材料的文种、格式、去口语化、降 AI 味时使用；适用于机关、企事业单位、学校、新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and writing teams use this skill to draft, revise, shorten, and review Chinese official documents, formal workplace materials, and news-style institutional copy. It helps check genre, format, formal tone, factual boundaries, handling elements, and AI-like phrasing for Chinese official writing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process user-provided official drafts that contain confidential or sensitive material.

Mitigation: Use it only in an agent environment approved for the sensitivity of the draft materials, and avoid providing confidential official materials otherwise.

Risk: Formal document drafting can introduce unsupported facts, policy claims, dates, amounts, or organizational conclusions if source material is incomplete.

Mitigation: Require users or reviewers to supply authoritative source facts and review final drafts for factual support before official use.

Risk: The optional local lint helper flags language, formatting, and repetition issues but does not determine legal, policy, or genre completeness on its own.

Mitigation: Treat lint output as advisory and keep human review for document genre, handling elements, institutional authority, and final approval.

## Reference(s):

- [中文公文写作](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [写作流程](references/workflow.md)
- [信息选择](references/information-selection.md)
- [文种路由](references/genre-routing.md)
- [办理要素](references/handling-elements.md)
- [论证链条](references/argument-chains.md)
- [公文语言风格](references/official-style.md)
- [公文行文用语](references/formulaic-language.md)
- [反 AI 表达检查](references/anti-ai-patterns.md)
- [总审层级](references/final-review-layers.md)
- [复核清单](references/review-checklist.md)
- [GB/T 9704-2012 常用格式参考](references/format-gbt9704.md)
- [AI 算力与技术服务材料](references/ai-compute-docs.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Plain text or Markdown, depending on the user's requested delivery format]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include drafted Chinese official-document text, revised copy, concise review findings, or format and style guidance]

## Skill Version(s):

1.6.21 (source: SKILL.md metadata, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
