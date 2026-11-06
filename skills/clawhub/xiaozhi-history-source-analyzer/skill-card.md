## Description:

按“读出处、提取信息、联系所学、得出结论”四步指导学生分析历史材料题，并帮助高中生对照史事和复盘错因。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

中学生可用它练习阅读史料、提取证据并组织历史材料题答案；高中生还可用它对照相近史事与概念，并分析答题错误。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student records, sharing, or reminders could expose information if enabled unnecessarily.

Mitigation: Use session-only mode by default; enable sharing and reminders only when needed, with guardian consent where required.

Risk: A connected record service could allow updates beyond the original history record.

Mitigation: Before connecting storage, ensure the receiving service restricts updates to the original history record; the bundled schema does not enforce this boundary.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-history-source-analyzer)
- [Source analysis guide](references/source-analysis-guide.md)
- [History error dimension table](references/history-error-dimension-table.md)
- [Required high school concepts](references/history-hs-concepts-required.md)
- [Elective high school concepts](references/history-hs-concepts-elective.md)
- [Required high school source examples](references/history-hs-sources-required.md)
- [Elective high school source examples](references/history-hs-sources-elective.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language conversational explanations and structured answer outlines]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adapts explanations to middle or high school history materials and the question asked.]

## Skill Version(s):

2.12.6 (source: server-resolved release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
