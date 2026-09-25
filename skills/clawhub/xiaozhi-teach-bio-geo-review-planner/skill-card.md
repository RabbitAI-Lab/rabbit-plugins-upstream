## Description:

帮助生物与地理教师依据本地当年的考试说明、课程标准及班级掌握情况，制定初中学业水平考试或高中合格性考试的复习计划。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

中国大陆的初高中生物与地理教师用它对照本地公开考试说明和班级掌握情况，安排考点复习、实验或地理实践及考前日程；生成内容须由教师审定。

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: An inaccurate or outdated exam scope could misdirect the review plan.

Mitigation: Use the teacher's public, current local exam guidance and flag any missing details for confirmation.

Risk: Sensitive student records or unreleased exam materials could be exposed.

Mitigation: Do not provide unreleased papers or identifiable student records; plan using aggregated topic-level information.

Risk: A review plan could be retained without the teacher's intent.

Mitigation: Require explicit confirmation before saving or changing plans, and provide viewing and deletion controls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-bio-geo-review-planner)
- [生地学业水平考试复习参考](references/bio-geo-exam-review.md)
- [实验安全约定](shared/lab-safety.md)
- [班级教学工作空间数据结构](https://xiaozhi-skills.openclaw.dev/schemas/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language tables and text review calendars]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review plans are saved only after teacher confirmation; text-only calendars are available without calendar access.]

## Skill Version(s):

2.4.0 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
