## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核；用户要求写申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、制度、规定、办法、管理办法、细则、操作规程、工作要点、总结、调研、讲话、致辞、可研、审查材料、AI 算力等正式文本，或需校验这类材料的文种、格式、去口语化、降 AI 味时使用；适用于机关、企事业单位、学校、新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees and external users use this skill to draft, revise, compress, and review Chinese official documents, formal workplace materials, and news-style institutional copy. It helps check genre, official-document structure, tone, formatting expectations, and unsupported factual claims before a draft is used.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential or sensitive draft content may be shared with the agent during writing or review.

Mitigation: Use only material appropriate for the deployment environment and remove unnecessary sensitive details before processing.

Risk: Generated official language, dates, amounts, signatures, seals, policy claims, or formatting may be incorrect or unsupported.

Mitigation: Review these elements against source materials and formal submission requirements before use.

## Reference(s):

- [中文公文写作](SKILL.md)
- [信息选择](references/information-selection.md)
- [任务路由卡](references/task-route-cards.md)
- [定向审稿清单](references/review-direct-checklist.md)
- [反 AI 表达检查](references/anti-ai-patterns.md)
- [办理要素](references/handling-elements.md)
- [总审层级](references/final-review-layers.md)
- [GB/T 9704-2012 常用格式参考](references/format-gbt9704.md)
- [短稿自然收束](references/short-draft-naturalness.md)
- [AI 写稿轻量校对](references/proofreading-checklist.md)
- [论证链条](references/argument-chains.md)
- [方案与建设方案 Playbook](references/genre-playbook-plan-construction.md)
- [写作流程](references/workflow.md)
- [文种与专项 Playbook](references/genre-playbooks.md)
- [公文语言风格](references/official-style.md)
- [AI 算力与技术服务材料](references/ai-compute-docs.md)
- [制度类文稿 Playbook](references/genre-playbook-institution-rules.md)
- [可行性研究报告细查](references/genre-checklist-feasibility-review.md)
- [请示/申请细查](references/genre-checklist-request.md)
- [会议纪要 Playbook](references/genre-playbook-minutes.md)
- [新闻消息](references/genre-playbook-news-message.md)
- [请示/申请 Playbook](references/genre-playbook-request.md)
- [新闻评论](references/genre-playbook-news-commentary.md)
- [文种清单](references/genre-checklist.md)
- [敬谦称谓和机关用语](references/formal-addressing.md)
- [函、复函与征求意见函 Playbook](references/genre-playbook-correspondence.md)
- [文种路由](references/genre-routing.md)
- [工作总结/工作要点/周报 Playbook](references/genre-playbook-work-summary.md)
- [公文行文用语](references/formulaic-language.md)
- [联网搜索与公开来源核验](references/external-research.md)
- [复核清单](references/review-checklist.md)
- [报告/情况说明 Playbook 与检查项](references/genre-checklist-report.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands]

**Output Format:** [Plain text or Markdown, with optional review findings and local lint commands when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Chinese official-document drafts, revised text, compression results, review comments, and formatting guidance; may coordinate DOCX handoff when formal Word output is requested.]

## Skill Version(s):

1.6.23 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
