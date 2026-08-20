## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核；用户要求写申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、征求意见函、制度、规定、办法、管理办法、实施细则、操作规程、工作要点、总结、调研、讲话、致辞、采购公告、可研、审查材料、AI 算力、新闻稿、新闻消息、快讯、活动报道、活动新闻稿、新闻通稿、新闻评论、时评、评论员文章等正式文本，或需校验这类材料的文种、格式、去口语化、降 AI 味时使用；适用于机关、企事业单位、学校、新闻机构。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and writing teams use this skill to draft, revise, compress, and review Chinese official documents, formal workplace materials, and news-style organizational texts. It helps preserve document type, official tone, formatting expectations, factual boundaries, and review checks for genres such as requests, reports, notices, letters, minutes, institutional rules, and AI compute procurement materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Drafts may contain incorrect official numbers, dates, signing details, or document-specific facts if the user-provided material is incomplete or inaccurate.

Mitigation: Verify official numbers, dates, signing details, policy references, and approvals against authoritative sources before final use.

Risk: The optional local lint script parses draft files supplied for review, which could expose unrelated private content if the wrong file is provided.

Mitigation: Run the lint script only on draft files intended for this task and avoid pointing it at unrelated private files.

Risk: The skill can improve tone and structure but does not independently validate the completeness of document-type elements or real-world facts.

Mitigation: Use the referenced genre, handling-element, and review checklists for final human review of document type, authority, facts, formatting, and approval readiness.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [Workflow](artifact/references/workflow.md)
- [Genre Routing](artifact/references/genre-routing.md)
- [Handling Elements](artifact/references/handling-elements.md)
- [Information Selection](artifact/references/information-selection.md)
- [Argument Chains](artifact/references/argument-chains.md)
- [Official Style](artifact/references/official-style.md)
- [Formulaic Language](artifact/references/formulaic-language.md)
- [Review Checklist](artifact/references/review-checklist.md)
- [Final Review Layers](artifact/references/final-review-layers.md)
- [Proofreading Checklist](artifact/references/proofreading-checklist.md)
- [Anti-AI Pattern Checks](artifact/references/anti-ai-patterns.md)
- [GB/T 9704 Format Reference](artifact/references/format-gbt9704.md)
- [AI Compute Documents](artifact/references/ai-compute-docs.md)
- [External Research and Public Source Checks](artifact/references/external-research.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Chinese prose, review notes, Markdown, and optional local lint command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide draft text, revision suggestions, document review findings, and optional prose-lint findings for user-supplied .txt, .md, or .docx drafts.]

## Skill Version(s):

1.6.11 (source: SKILL.md frontmatter metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
