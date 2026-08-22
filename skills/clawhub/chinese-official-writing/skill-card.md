## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核；用户要求写申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、制度、规定、办法、管理办法、实施细则、操作规程、工作要点、总结、调研、讲话、致辞、可研、审查材料、AI 算力等正式文本，或需校验这类材料的文种、格式、去口语化、降 AI 味时使用；适用于机关、企事业单位、学校、新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees and external users use this skill to draft, revise, compress, and review Chinese official documents, workplace materials, and news-style releases. It helps check document genre, structure, formal tone, formatting expectations, and AI-like phrasing while preserving user-provided facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process official-document text provided by the user, which can include sensitive workplace or organizational details.

Mitigation: Users should review input text for confidential content and follow their organization's data-handling policy before using the skill.

Risk: Public-source verification is used only when requested or when current facts are necessary, so unsupported current facts can remain unverified if the user does not ask for verification.

Mitigation: Ask for public-source verification when documents depend on current policies, dates, statistics, or other time-sensitive facts.

## Reference(s):

- [写作流程](references/workflow.md)
- [文种路由](references/genre-routing.md)
- [办理要素](references/handling-elements.md)
- [信息选择](references/information-selection.md)
- [论证链条](references/argument-chains.md)
- [公文语言风格](references/official-style.md)
- [复核清单](references/review-checklist.md)
- [反 AI 表达检查](references/anti-ai-patterns.md)
- [GB/T 9704-2012 常用格式参考](references/format-gbt9704.md)
- [联网搜索与公开来源核验](references/external-research.md)
- [AI 算力与技术服务材料](references/ai-compute-docs.md)
- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Plain text or Markdown, with code and shell commands only when needed for local prose linting or requested delivery.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce formal Chinese document drafts, revised text, review notes, formatting guidance, or optional local lint command suggestions.]

## Skill Version(s):

1.6.13 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
