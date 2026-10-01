## Description:

帮助中国大陆中小学教师依据班级薄弱点制定知识图谱、分阶段复习策略与间隔回看排期。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

中小学教师使用本技能梳理知识点和班级共性弱项，制定单元、期中或期末复习计划，包括阶段安排、间隔回看和交叉练习。技能提供教师审定的草稿，不代替教学评价或生成整套作业、试卷。

### Deployment Geography for Use:

Chinese mainland (localization required elsewhere)

## Known Risks and Mitigations:

Risk: Classroom learning data and student identities may be exposed in review plans.

Mitigation: Read only relevant class-level data; require teacher approval before saving, use pseudonyms, and exclude individual scores and rankings.

Risk: Curriculum, privacy expectations, and crisis contacts may not fit other locales.

Mitigation: Localize curriculum assumptions, privacy practices, and crisis-referral contacts before use outside Chinese mainland.

Risk: AI-generated review examples or schedules may be inaccurate.

Mitigation: Have the teacher review plans and verify generated examples before use; do not promise exam outcomes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-review-planner)
- [Review strategy](references/review-strategy.md)
- [Knowledge map example](references/knowledge-map-example.md)
- [Key points checklist template](references/key-points-checklist-template.md)
- [Review activity library](references/review-activity-library.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown tables and text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Knowledge maps and dated review schedules; saves plans only after teacher approval.]

## Skill Version(s):

2.9.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
