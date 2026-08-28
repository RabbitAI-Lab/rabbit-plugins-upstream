## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核；用户要求写申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、制度、规定、办法、管理办法、细则、操作规程、工作要点、总结、调研、讲话、致辞、可研、审查材料、AI 算力等正式文本，或需校验这类材料的文种、格式、去口语化、降 AI 味时使用；适用于机关、企事业单位、学校、新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and professional writers use this skill to draft, revise, condense, and review Chinese official documents, formal workplace materials, and news-style institutional copy. It helps check genre fit, document structure, official tone, formatting expectations, factual boundaries, and anti-AI-style language risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Official-document drafts may contain inaccurate facts, dates, authority claims, or unsupported conclusions if source material is incomplete.

Mitigation: Review every generated document against authoritative source material before circulation or filing.

Risk: Formal workplace and official documents may include confidential or sensitive organizational information.

Mitigation: Use the skill only with information appropriate for the agent environment and follow the organization's confidentiality review process before sharing outputs.

Risk: The optional local lint script checks draft prose and may process document text supplied to it.

Mitigation: Run linting only on drafts intended for review in the local environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [AI 算力与技术服务材料](references/ai-compute-docs.md)
- [反 AI 表达检查](references/anti-ai-patterns.md)
- [论证链条](references/argument-chains.md)
- [联网搜索与公开来源核验](references/external-research.md)
- [总审层级](references/final-review-layers.md)
- [敬谦称谓和机关用语](references/formal-addressing.md)
- [GB/T 9704-2012 常用格式参考](references/format-gbt9704.md)
- [公文行文用语](references/formulaic-language.md)
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

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Plain text or Markdown, with optional local lint shell commands when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce official-document drafts, revised text, review findings, formatting guidance, or lint results depending on the user request.]

## Skill Version(s):

1.6.19 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
