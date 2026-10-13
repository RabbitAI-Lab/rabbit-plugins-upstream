## Description:

为中国大陆中小学生制定可执行的学习计划：小学高段按周安排，初高中按30天安排，并在学生开启后跟进执行情况。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in upper primary, middle and high school use this skill to turn goals and weak-subject summaries into manageable weekly or 30-day study schedules and exam preparation plans. Upper-primary students use it with a parent or teacher present; family dashboards and progress follow-up are optional.

### Deployment Geography for Use:

Mainland China (Simplified Chinese K12 learning context); localize emergency contacts, curriculum and minor-consent rules before use elsewhere.

## Known Risks and Mitigations:

Risk: Using mainland China curriculum assumptions or emergency contacts outside their intended region may misdirect students.

Mitigation: Restrict use to the Simplified Chinese mainland K12 context until curriculum, emergency contacts and minor-consent requirements are localized.

Risk: Learning-profile access, family dashboards or reminders could expose a minor's information without appropriate consent.

Mitigation: Keep each capability off by default; obtain separate opt-in before access, parent-visible sharing or reminder queuing, and apply guardian-consent requirements for younger students.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-plan)
- [Study plan templates](references/plan-templates.md)
- [Grade-band guidance](shared/grade-bands.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese text and Markdown study schedules and optional family dashboard]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Upper-primary weekly plans; middle- and high-school 30-day plans; optional progress reviews and parent-visible summaries.]

## Skill Version(s):

2.11.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
