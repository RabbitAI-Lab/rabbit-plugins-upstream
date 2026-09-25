## Description:

为中国大陆小学高段至高中学生制定可执行的学习计划，并在学生同意后跟进完成情况。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in mainland China's upper-primary, middle-school and high-school grades use this skill to schedule study and exam preparation. It provides weekly plans for upper-primary students and 30-day plans for older students, with optional progress check-ins and parent-facing task boards.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: A minor's learning profile, completion updates or plan could be used or retained without appropriate permission.

Mitigation: Require the documented student and, where applicable, guardian consent before accessing profiles or saving plans; allow students to review, correct, export and delete their records, and limit retention of completion updates.

Risk: Parent-visible task boards or queued reminders could share information or contact a minor unexpectedly.

Mitigation: Enforce separate consent for parent views and reminder requests, honor a student's decision not to share, and include only tasks and completion status in parent boards.

Risk: Mainland China-specific school and crisis guidance may be unsuitable elsewhere.

Mitigation: Restrict deployment to the documented Chinese K12 setting unless local school guidance, emergency contacts and minor-consent requirements are reviewed and adapted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-plan)
- [Study plan templates](artifact/references/plan-templates.md)
- [Grade-band guidance](artifact/shared/grade-bands.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language study schedules, weekly progress summaries and optional parent-facing task boards in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Upper-primary students receive a weekly plan; middle- and high-school students receive a 30-day plan. Parent views and reminder requests require separate consent.]

## Skill Version(s):

2.4.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
