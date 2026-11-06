## Description:

为中学数学教师提供测评蓝图与双向细目表、选题和版权标注、逐题统计，并整理经教师逐条确认的写回内容。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

中学数学教师可用它设计诊断性、形成性或终结性测评蓝图，标注题目来源与版权，并分析逐题难度和区分度。它要求教师审核 AI 起草题目和写回内容。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The report template and data schema conflict with the skill’s stated privacy limits when connecting student records.

Mitigation: Before using real records, remove historical fields from the report template and reconcile the schema with the read allowlist.

Risk: Student records could be exposed or used beyond the intended aggregate analysis and approved sharing.

Mitigation: Use aggregate tier counts without student mappings, and keep teacher approval for saving and sharing results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-exam-designer)
- [Blueprint template](artifact/references/blueprint-template.md)
- [Exam design process](artifact/references/exam-design-process.md)
- [Result analysis rubric](artifact/references/result-analysis-rubric.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Analysis, JSON]

**Output Format:** [Markdown blueprints, tables, and reports; structured JSON fields for confirmed workspace entries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Candidate questions require teacher verification before use; workspace writeback requires item-by-item teacher approval.]

## Skill Version(s):

2.12.6 (source: SKILL.md frontmatter, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
