## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核；用户要求写申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、征求意见函、制度、规定、办法、管理办法、实施细则、操作规程、工作要点、总结、调研、讲话、致辞、采购公告、可研、审查材料、AI 算力、新闻稿、新闻消息、快讯、活动报道、活动新闻稿、新闻通稿、新闻评论、时评、评论员文章等正式文本，或需校验这类材料的文种、格式、去口语化、降 AI 味时使用；适用于机关、企事业单位、学校、新闻机构。不用于英文、文学、营销、社媒、论文或个人求职。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees and external users who prepare Chinese official documents, workplace materials, and news-style institutional writing can use this skill to draft, revise, compress, and review formal Chinese texts. It supports genre routing, official-document structure, GB/T 9704-style formatting guidance, language cleanup, and risk-focused review for provided facts and user-supplied materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive government, business, or personal content may be included in official-document drafting or review prompts.

Mitigation: Use the skill only in approved environments and provide only documents the agent is intended to read.

Risk: Drafted or revised official materials can become misleading if unsupported facts, dates, amounts, units, or policy claims are introduced.

Mitigation: Keep source facts traceable to user-provided materials and review final drafts before use or circulation.

Risk: The included prose lint script reads files supplied to it.

Mitigation: Run the script only on local files intended for agent review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [写作流程](references/workflow.md)
- [文种路由](references/genre-routing.md)
- [文种清单](references/genre-checklist.md)
- [复核清单](references/review-checklist.md)
- [反 AI 表达检查](references/anti-ai-patterns.md)
- [GB/T 9704-2012 常用格式参考](references/format-gbt9704.md)
- [联网搜索与公开来源核验](references/external-research.md)
- [AI 算力与技术服务材料](references/ai-compute-docs.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands]

**Output Format:** [Chinese prose, Markdown review notes, and optional shell commands for local prose linting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve supplied facts, avoid unsupported claims, and distinguish drafting, revision, review, and formatting tasks.]

## Skill Version(s):

1.6.9 (source: ClawHub release metadata and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
