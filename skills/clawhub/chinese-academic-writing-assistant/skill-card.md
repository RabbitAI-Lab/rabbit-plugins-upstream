## Description:

中文论文写作 helps agents draft, revise, review, and source-check Chinese undergraduate, master's, course-paper, proposal, and standalone literature-review work from user-provided materials or explicitly authorized source searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to structure, draft, revise, and review Chinese academic writing while preserving the boundaries of supplied evidence, institutional templates, and explicitly authorized source lookup. It is intended for academic writing assistance, citation/source checking, long-form consistency review, and localized prose quality review, not for fabricating research, citations, data, results, or authorship.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive theses, unpublished drafts, source materials, or research notes may be exposed to the agent or to external lookup workflows if the user provides them.

Mitigation: Share only the files needed for the task, keep sensitive material out of scope when possible, and authorize source searches only for clearly bounded topics and rounds.

Risk: Academic prose can become misleading if the agent fills gaps with unsupported facts, fabricated citations, or stronger conclusions than the materials justify.

Mitigation: Use the skill's material gates, source-status distinctions, citation checks, and downgrade behavior so unsupported content is omitted, narrowed, or moved to explicit follow-up suggestions.

Risk: Local audit scripts can surface candidate issues that may be mistaken for verified writing, citation, or format errors.

Mitigation: Treat script findings as review candidates only and confirm each issue against the draft, source materials, and institutional requirements before changing content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-academic-writing-assistant)
- [普通中文论文专项叶](references/academic-writing.md)
- [中文论文开题报告专项叶](references/academic-proposal.md)
- [中文论文独立文献综述专项叶](references/academic-literature-review.md)
- [学术来源检索与引用覆盖](references/citation-research.md)
- [长稿一致性](references/long-form-consistency.md)
- [论文 ANTI-AI 语义复核](references/anti-ai-writing.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Chinese prose, Markdown outlines or review tables, and optional shell command snippets for local audit scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include scoped source-review notes, citation coverage findings, manuscript consistency findings, or prose-quality review notes when the user asks for those modes.]

## Skill Version(s):

0.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
