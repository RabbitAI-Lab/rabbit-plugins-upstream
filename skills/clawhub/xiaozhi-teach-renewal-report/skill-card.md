## Description:

用学员真实的学习记录生成阶段报告和续课建议，帮助独立教师以事实、进步和计划回应家长沟通。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

独立教师使用该技能为指定学员整理阶段学习报告、续课报告和家长沟通草稿。它读取已授权的课后记录、作业跟进、进步证据和课时信息，并要求老师审定后手动发送。

### Deployment Geography for Use:

Mainland China by default; localize curriculum, law, consent, and emergency-help channels before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill handles minors' longitudinal learning records when drafting reports.

Mitigation: Confirm workspace consent fields, use aliases, read only the named student's relevant records, and keep parent-visible output teacher-reviewed.

Risk: Unsupported progress claims could mislead parents about learning outcomes.

Mitigation: Include only facts backed by records, avoid inferred percentages and score promises, and mark insufficient samples as observations rather than conclusions.

Risk: The workflow is designed for Chinese K12 independent-teacher use.

Mitigation: Before use outside Mainland China, localize curriculum assumptions, legal consent requirements, language, and emergency-help channels.

## Reference(s):

- [Stage report templates](references/stage-report-templates.md)
- [Renewal communication scripts](references/renewal-communication-scripts.md)
- [Platform conventions](shared/platform-conventions.md)
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-renewal-report)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese Markdown/text report drafts and communication scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-reviewed drafts only; no automatic sending, scheduling, or student-record status changes.]

## Skill Version(s):

2.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
