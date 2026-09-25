## Description:

帮助中国中小学教师根据班级学情制定有重点的复习计划，包括知识图谱、间隔回看、交叉练习和考前安排。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to prioritize classroom review topics and draft unit or exam review schedules from scoped class learning data. Teachers review the plans and explicitly approve any saved schedule.

### Deployment Geography for Use:

Mainland China; localize curriculum, language, and crisis-referral channels before use elsewhere.

## Known Risks and Mitigations:

Risk: Class learning data or individual student details could be disclosed in review materials or saved plans.

Mitigation: Read only task-relevant class data, use pseudonyms, omit individual scores and rankings, and require teacher confirmation before saving or changing plans.

Risk: Curriculum assumptions and crisis-referral information may be unsuitable outside Mainland China.

Mitigation: Localize curriculum, language, and referral channels before use in another region.

Risk: AI-generated example questions or student-facing guidance may contain errors.

Mitigation: Check generated questions and have teachers approve material before sharing it with students or families.

## Reference(s):

- [Review strategies and schedules](references/review-strategy.md)
- [Knowledge map example](references/knowledge-map-example.md)
- [Key points checklist template](references/key-points-checklist-template.md)
- [Review activity library](references/review-activity-library.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration]

**Output Format:** [Markdown review plans, knowledge maps, and dated schedules; structured plan data only after teacher confirmation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides planning rather than full assignment sets or exam papers; teachers review student-facing material.]

## Skill Version(s):

2.4.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
