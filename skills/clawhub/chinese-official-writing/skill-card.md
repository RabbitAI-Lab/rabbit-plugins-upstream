## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核；用户要求写申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、制度、规定、办法、管理办法、细则、操作规程、工作要点、总结、调研、讲话、致辞、可研、审查材料、AI 算力等正式文本，或需校验这类材料的文种、格式、去口语化、降 AI 味时使用；适用于机关、企事业单位、学校、新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, public-sector staff, enterprise teams, schools, and news organizations use this skill to draft, revise, shorten, and review Chinese official documents, formal workplace materials, and news-style releases. It helps check document genre, writing relationship, official tone, factual boundaries, formatting expectations, and AI-like phrasing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Drafts or review guidance may be mistaken for authoritative legal, policy, document-office, or organizational approval.

Mitigation: Use the skill for drafting and review assistance only; responsible humans or organizations should approve final facts, wording, and compliance decisions.

Risk: Official documents may contain incorrect or unsupported facts, citations, seals, dates, signatures, formatting, or approval conclusions if inputs are incomplete.

Mitigation: Verify all facts, cited sources, dates, signatures, seals, red-head formatting, and document-office requirements against authoritative materials before release.

Risk: A generated formal text may overstate decisions, implementation status, responsibilities, or next steps beyond the user's evidence.

Mitigation: Constrain final text to provided materials and explicitly review whether claims, action items, and document genre match the available evidence and intended writing relationship.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [Publisher Profile](https://clawhub.ai/user/gongyu0918-debug)
- [写作流程](references/workflow.md)
- [文种路由](references/genre-routing.md)
- [信息选择](references/information-selection.md)
- [办理要素](references/handling-elements.md)
- [公文语言风格](references/official-style.md)
- [总审层级](references/final-review-layers.md)
- [复核清单](references/review-checklist.md)
- [GB/T 9704-2012 常用格式参考](references/format-gbt9704.md)
- [反 AI 表达检查](references/anti-ai-patterns.md)
- [AI 算力与技术服务材料](references/ai-compute-docs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Plain text or Markdown, with optional review notes, lint findings, and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve user-provided facts and structure; official facts, citations, seals, dates, signatures, red-head formatting, and final compliance decisions require human or organizational review.]

## Skill Version(s):

1.6.15 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
