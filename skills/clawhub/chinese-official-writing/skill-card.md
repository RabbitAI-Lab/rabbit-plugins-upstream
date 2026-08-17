## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核，并在用户需要时校验文种、格式、去口语化和降低 AI 痕迹。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees and external users in agencies, enterprises, schools, and news organizations use this skill to draft, revise, compress, and review Chinese official documents, work materials, and formal news-style copy. It supports document-type routing, handling-element checks, formal tone review, GB/T 9704-oriented formatting guidance, and optional lint-style review of Chinese drafts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Official drafts may contain sensitive business or institutional information.

Mitigation: Use the skill and its linting behavior only with text or files the user intends the agent to read.

Risk: Generated official text may include incorrect, unsupported, or unapproved statements if the source material is incomplete.

Mitigation: Review generated drafts before submission or publication, and verify facts, approvals, dates, amounts, and policy references against authoritative sources.

## Reference(s):

- [中文公文写作](SKILL.md)
- [写作流程](references/workflow.md)
- [文种路由](references/genre-routing.md)
- [办理要素](references/handling-elements.md)
- [信息选择](references/information-selection.md)
- [文种与专项 Playbook](references/genre-playbooks.md)
- [GB/T 9704-2012 常用格式参考](references/format-gbt9704.md)
- [复核清单](references/review-checklist.md)
- [反 AI 表达检查](references/anti-ai-patterns.md)
- [AI 写稿轻量校对](references/proofreading-checklist.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown with optional review findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include draft text, revised text, compressed text, issue locations, risk levels, and modification suggestions; generated official text should be reviewed before submission or publication.]

## Skill Version(s):

1.6.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
