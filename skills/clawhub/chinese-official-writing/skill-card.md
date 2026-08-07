## Description:

用于中文公文和机关企事业单位、学校等正式事务材料的起草、改写、压缩和复核；当用户明确要求写申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、征求意见函、制度、规定、办法、管理办法、实施细则、操作规程、工作要点、总结、调研、讲话、致辞、采购公告、可研、审查材料、AI 算力、新闻稿、新闻消息、快讯、活动报道、活动新闻稿、新闻通稿、新闻评论、时评、评论员文章等正式文本，或要求对这类材料做文种校验、格式核验、去口语化、降 AI 味时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external contributors, and agent users use this skill to draft, revise, compress, and review Chinese official documents and formal work materials. It helps route document genres, preserve required handling elements, reduce informal or AI-like wording, and flag issues that still need human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive draft content may be processed by the agent or printed as excerpts by the optional local lint script.

Mitigation: Run the skill and lint script only on documents intended for agent review, and avoid sharing restricted or confidential material unless that use is approved.

Risk: Generated or revised wording could affect legal, financial, procurement, audit, or formal signing decisions.

Mitigation: Require accountable human review before relying on the output for approvals, submissions, signing, procurement, or audit-related decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [GitHub Repository README](https://github.com/gongyu0918-debug/chinese-official-writing-skill)
- [Issue Tracker](https://github.com/gongyu0918-debug/chinese-official-writing-skill/issues)
- [Workflow](references/workflow.md)
- [Genre Routing](references/genre-routing.md)
- [Handling Elements](references/handling-elements.md)
- [Review Checklist](references/review-checklist.md)
- [GB/T 9704 Formatting](references/format-gbt9704.md)
- [Anti-AI Patterns](references/anti-ai-patterns.md)
- [AI Compute Documents](references/ai-compute-docs.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Chinese prose, Markdown review notes, optional shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use an optional local prose lint script that prints matched excerpts to terminal output.]

## Skill Version(s):

1.5.38 (source: evidence release, SKILL.md frontmatter, README)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
