## Description:

为中国语境下的中小学生制定可执行的学习计划：小学高段按周安排，初高中按 30 天安排，并在学生开启后跟进执行情况。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

学生用它把学习目标和可用时间转成每周或 30 天的具体任务，并在选择开启后查看执行进度。家长可在学生单独同意后查看仅含任务和完成情况的看板；小学高段需家长或老师陪同使用。

### Deployment Geography for Use:

Global; Chinese-language content requires localization for other regions.

## Known Risks and Mitigations:

Risk: Student learning records, saved plans, parent sharing, or reminders could be used without the required permissions.

Mitigation: Confirm the student's and, where required, guardian's understanding and obtain separate consent before enabling each feature; keep them off by default.

Risk: Chinese K12 defaults for consent and support resources may not fit other regions.

Mitigation: Use only in the intended setting or localize consent requirements and support resources before deployment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-plan)
- [Study plan templates](artifact/references/plan-templates.md)
- [Grade-band guidance](artifact/shared/grade-bands.md)
- [Consent and sharing conventions](artifact/shared/vocab.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Weekly or 30-day task schedules, progress summaries, and optional parent-facing task/completion views; profile access, parent sharing, and reminder queueing require separate consent.]

## Skill Version(s):

2.8.0 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
