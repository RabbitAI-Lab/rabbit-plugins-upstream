## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核；用户要求写申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、制度、规定、办法、管理办法、细则、操作规程、工作要点、总结、调研、讲话、致辞、可研、审查材料、AI 算力等正式文本，或需校验这类材料的文种、格式、去口语化、降 AI 味时使用；适用于机关、企事业单位、学校、新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and developers use this skill to draft, revise, compress, and review Chinese official documents, work materials, and news-style formal writing. It helps check document genre, format, official style, factual boundaries, and AI-like wording for organizations such as agencies, enterprises, schools, and news institutions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Internal drafts or DOCX files provided to the agent may contain sensitive organizational information.

Mitigation: Use the skill only with documents intended for agent processing, and avoid providing confidential material that the agent should not read.

Risk: The optional lint script scans document text and may surface content from files supplied for review.

Mitigation: Run the lint script only on documents the user intends to scan and review its findings before acting on them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [写作流程](references/workflow.md)
- [文种路由](references/genre-routing.md)
- [信息选择](references/information-selection.md)
- [办理要素](references/handling-elements.md)
- [文种与专项 Playbook](references/genre-playbooks.md)
- [复核清单](references/review-checklist.md)
- [反 AI 表达检查](references/anti-ai-patterns.md)
- [公文语言风格](references/official-style.md)
- [GB/T 9704-2012 常用格式参考](references/format-gbt9704.md)
- [AI 算力与技术服务材料](references/ai-compute-docs.md)
- [联网搜索与公开来源核验](references/external-research.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown prose with optional review notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce complete Chinese formal drafts, revised text, condensed text, or issue-focused review guidance.]

## Skill Version(s):

1.6.24 (source: SKILL.md metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
