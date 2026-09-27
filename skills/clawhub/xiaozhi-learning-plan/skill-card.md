## Description:

为小学高段学生安排每周学习任务，为初高中学生制定并跟进 30 天学习计划。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向小学高段、初中及高中学生，结合学习目标和可用时间安排具体任务，并在学生选择开启后跟进完成情况；小学高段使用周计划。

### Deployment Geography for Use:

Mainland China; localize crisis contacts, school grades, curriculum, and minor/guardian consent rules before use elsewhere.

## Known Risks and Mitigations:

Risk: Student learning information could be shared or used beyond the student's expectations.

Mitigation: Obtain separate explicit consent for profile access, parent-facing boards, and reminders; review permissions with students and guardians where applicable.

Risk: Mainland China-specific crisis contacts, school-grade assumptions, or consent rules may be inappropriate elsewhere.

Mitigation: Confirm the deployment region and localize crisis contacts, grade mappings, curriculum, and guardian-consent rules before use outside mainland China.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-plan)
- [Learning plan templates](artifact/references/plan-templates.md)
- [Grade-band guidance](artifact/shared/grade-bands.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown study plans and optional progress summaries or parent-facing task boards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Weekly plans for upper primary; 30-day plans for middle and high school. Profile access, parent sharing, and reminders each require separate consent.]

## Skill Version(s):

2.7.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
