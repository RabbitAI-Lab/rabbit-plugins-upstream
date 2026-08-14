## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核；用户要求写申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、征求意见函、制度、规定、办法、管理办法、实施细则、操作规程、工作要点、总结、调研、讲话、致辞、采购公告、可研、审查材料、AI 算力、新闻稿、新闻消息、快讯、活动报道、活动新闻稿、新闻通稿、新闻评论、时评、评论员文章等正式文本，或需校验这类材料的文种、格式、去口语化、降 AI 味时使用；适用于机关、企事业单位、学校、新闻机构。不用于英文、文学、营销、社媒、论文或个人求职。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, writers, reviewers, and external users can use this skill to draft, revise, compress, format-check, and review Chinese official documents, formal workplace materials, and news-style institutional texts. It is intended for supported Chinese document genres and excludes English writing, literary writing, marketing copy, social media posts, academic papers, and personal job applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential drafts, DOCX files, or government and business materials may contain sensitive information.

Mitigation: Only provide documents and excerpts the agent is intended to inspect, and remove unnecessary confidential details before use.

Risk: Official documents can become misleading if unsupported facts, dates, policy claims, amounts, or approvals are added.

Mitigation: Require user-provided source material for factual claims and have a human reviewer confirm the final text before circulation or signature.

Risk: The optional prose lint script inspects files named by the user.

Mitigation: Run linting only on drafts selected for inspection and treat lint output as guidance rather than an automatic rewrite.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [信息选择](references/information-selection.md)
- [任务路由卡](references/task-route-cards.md)
- [写作流程](references/workflow.md)
- [文种路由](references/genre-routing.md)
- [办理要素](references/handling-elements.md)
- [论证链条](references/argument-chains.md)
- [公文语言风格](references/official-style.md)
- [复核清单](references/review-checklist.md)
- [总审层级](references/final-review-layers.md)
- [AI 写稿轻量校对](references/proofreading-checklist.md)
- [反 AI 表达检查](references/anti-ai-patterns.md)
- [GB/T 9704-2012 常用格式参考](references/format-gbt9704.md)
- [联网搜索与公开来源核验](references/external-research.md)
- [文种与专项 Playbook](references/genre-playbooks.md)
- [报告/情况说明 Playbook 与检查项](references/genre-checklist-report.md)
- [请示/申请 Playbook](references/genre-playbook-request.md)
- [制度类文稿 Playbook](references/genre-playbook-institution-rules.md)
- [新闻消息](references/genre-playbook-news-message.md)
- [新闻评论](references/genre-playbook-news-commentary.md)
- [AI 算力与技术服务材料](references/ai-compute-docs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown, depending on the requested delivery]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include review findings, rewrite suggestions, formal document drafts, compressed versions, or formatting guidance; optional local linting only inspects files the user names.]

## Skill Version(s):

1.6.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
