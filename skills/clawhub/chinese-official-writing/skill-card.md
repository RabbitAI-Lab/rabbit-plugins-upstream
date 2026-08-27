## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核；用户要求写申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、制度、规定、办法、管理办法、细则、操作规程、工作要点、总结、调研、讲话、致辞、可研、审查材料、AI 算力等正式文本，或需校验这类材料的文种、格式、去口语化、降 AI 味时使用；适用于机关、企事业单位、学校、新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees and external users use this skill to draft, revise, compress, and review Chinese official documents, formal workplace materials, and news-style organizational copy. It helps preserve document genre, official tone, formatting expectations, and fact boundaries when working from user-provided materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process sensitive or draft official-document content supplied by the user.

Mitigation: Review inputs before use and avoid providing confidential, regulated, or non-public information unless the deployment environment is approved for that data.

Risk: Generated official documents can include incorrect facts if source materials are incomplete or if current public facts are needed.

Mitigation: Use the skill's fact-bound drafting posture, verify dates, amounts, policies, names, and public-source claims before release, and request lookup only when current or external facts are required.

Risk: The optional local prose linter reports language and formatting signals, not authoritative genre or policy compliance.

Mitigation: Treat lint output as review guidance and have a qualified reviewer confirm document genre, approval posture, formatting, and organizational requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [Workflow](references/workflow.md)
- [Information Selection](references/information-selection.md)
- [Genre Routing](references/genre-routing.md)
- [Handling Elements](references/handling-elements.md)
- [Argument Chains](references/argument-chains.md)
- [Official Style](references/official-style.md)
- [Final Review Layers](references/final-review-layers.md)
- [Review Checklist](references/review-checklist.md)
- [GB/T 9704 Formatting](references/format-gbt9704.md)
- [External Research](references/external-research.md)
- [AI Compute Documents](references/ai-compute-docs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Plain text or Markdown, with optional code or shell command blocks when the task calls for file checks or configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May process user-provided draft text or files; includes an optional local prose-lint script for specified text, Markdown, or DOCX drafts.]

## Skill Version(s):

1.6.18 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
