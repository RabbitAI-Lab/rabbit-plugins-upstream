## Description:

Drafts, revises, compresses, and reviews Chinese official and formal workplace documents, including requests, reports, notices, plans, minutes, rules, AI-compute materials, and related review tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and writing agents use this skill to draft or review Chinese official documents and formal work materials while preserving document genre, writing relationship, factual boundaries, required handling elements, and formal tone.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Drafts for legal, finance, procurement, audit, or formally signed materials may contain incorrect facts, missing approvals, or unsuitable conclusions if used without review.

Mitigation: Treat output as drafting assistance and review facts, approvals, dates, amounts, sign-off requirements, and final conclusions before use.

Risk: Formal document formatting or genre choices may not match a user's local institutional rules or current official requirements.

Mitigation: Check the selected genre, document relationship, required handling elements, and formatting against the user's authoritative template or policy before issuing the document.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [中文公文写作 Skill README](README.md)
- [写作流程](references/workflow.md)
- [文种路由](references/genre-routing.md)
- [办理要素](references/handling-elements.md)
- [反 AI 表达检查](references/anti-ai-patterns.md)
- [复核清单](references/review-checklist.md)
- [GB/T 9704-2012 常用格式参考](references/format-gbt9704.md)
- [AI 算力与技术服务材料](references/ai-compute-docs.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands]

**Output Format:** [Chinese plain text or Markdown drafts, review notes, revision guidance, and optional local lint command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May route to reference playbooks and an optional local prose lint script for draft review; script findings are advisory and do not rewrite text automatically.]

## Skill Version(s):

1.5.41 (source: SKILL.md metadata, README, and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
