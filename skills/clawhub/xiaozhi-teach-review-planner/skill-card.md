## Description:

把“从头再讲一遍”变成有间隔、有交叉、有取舍的复习排期。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to plan Chinese-language unit, midterm, final, and pre-exam review schedules. It helps organize knowledge maps, priority topics, spaced review, interleaved practice groups, review activities, and pre-exam state guidance while leaving concrete assignments and exams to adjacent skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The crisis-referral instructions include mainland China emergency and youth-support contacts, which may be inappropriate outside that region.

Mitigation: Review and replace crisis-referral contacts before deployment outside mainland China, or limit deployment to contexts where those contacts are appropriate.

Risk: Review plan writebacks and student learning data could expose sensitive student performance information if used without controls.

Mitigation: Keep reviewPlans teacher-confirmed, use aliases or aggregate weakness data, and avoid exposing individual scores or rankings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-review-planner)
- [复习策略：间隔回看与交叉练习排期](references/review-strategy.md)
- [重难点清单模板](references/key-points-checklist-template.md)
- [知识图谱可视化范例](references/knowledge-map-example.md)
- [复习活动设计样例库](references/review-activity-library.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [Crisis exception protocol](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured planning guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose teacher-confirmed reviewPlans entries, including phases, spacing schedules, interleaving sets, and source weakness identifiers.]

## Skill Version(s):

2.1.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
