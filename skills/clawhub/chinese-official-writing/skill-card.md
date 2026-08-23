## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核；用户要求写申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、制度、规定、办法、管理办法、实施细则、操作规程、工作要点、总结、调研、讲话、致辞、可研、审查材料、AI 算力等正式文本，或需校验这类材料的文种、格式、去口语化、降 AI 味时使用；适用于机关、企事业单位、学校、新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees and external users use this skill to draft, revise, shorten, format, and review formal Chinese official documents, business materials, institutional rules, news releases, and AI compute-related formal texts. It helps check genre fit, official-document structure, tone, factual boundaries, GB/T 9704-style formatting needs, and signs of formulaic or AI-like wording.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be used with sensitive business, internal, or official Chinese documents.

Mitigation: Use the same access controls and review practices applied to internal document drafting, and avoid sharing text the agent should not read.

Risk: The optional lint script reads files supplied to it for prose analysis.

Mitigation: Run the lint script only on documents intended for agent review and inspect findings before applying changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [写作流程](references/workflow.md)
- [文种路由](references/genre-routing.md)
- [文种与专项 Playbook](references/genre-playbooks.md)
- [办理要素](references/handling-elements.md)
- [信息选择](references/information-selection.md)
- [复核清单](references/review-checklist.md)
- [反 AI 表达检查](references/anti-ai-patterns.md)
- [GB/T 9704-2012 常用格式参考](references/format-gbt9704.md)
- [AI 算力与技术服务材料](references/ai-compute-docs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown, with optional review notes or shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce formal Chinese drafts, revised text, concise review findings, formatting guidance, or local lint findings; no fixed token cap.]

## Skill Version(s):

1.6.14 (source: SKILL.md metadata and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
