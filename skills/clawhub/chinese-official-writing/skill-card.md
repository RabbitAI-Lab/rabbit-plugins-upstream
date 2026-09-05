## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核，并帮助校验文种、格式、公文语气和降 AI 味。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and professional writers use this skill to draft, revise, shorten, and review Chinese official documents, formal work materials, and news-style organizational copy. It is suited to government, enterprise, school, and newsroom workflows that need formal Chinese document structure and style checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional local linter can read draft files supplied by the user, including DOCX text and comments.

Mitigation: Run the linter only on files intended for review, and avoid pointing it at unrelated or sensitive drafts.

Risk: The skill is scoped to Chinese official documents and formal work materials, not English writing or general creative writing.

Mitigation: Use it only for the supported Chinese formal-writing scenarios, and route unrelated writing tasks to a more appropriate skill.

Risk: Formal documents may contain unsupported facts, dates, amounts, approval conclusions, or organizational claims if source material is incomplete.

Mitigation: Review generated drafts against the provided source material and confirm official facts before submitting or publishing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [写作流程](references/workflow.md)
- [文种路由](references/genre-routing.md)
- [办理要素](references/handling-elements.md)
- [GB/T 9704-2012 常用格式参考](references/format-gbt9704.md)
- [AI 写稿轻量校对](references/proofreading-checklist.md)
- [联网搜索与公开来源核验](references/external-research.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown, with optional code or shell commands when running local draft checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use an optional local linter for Chinese draft files, including TXT, Markdown, and DOCX inputs.]

## Skill Version(s):

1.6.26 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
