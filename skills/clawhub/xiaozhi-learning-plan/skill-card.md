## Description:

Creates practical 30-day study plans for Chinese middle- and high-school students, or weekly plans for upper-primary students, and helps adjust them as progress changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese K–12 students use this skill to turn study goals and available time into manageable daily or weekly tasks, with optional progress reviews and a parent-visible task dashboard. Upper-primary students use it with a parent or teacher present.

### Deployment Geography for Use:

Mainland China (default; localize crisis referral information before use elsewhere)

## Known Risks and Mitigations:

Risk: Student profile details, task progress, or reminders could be used or shared without the student's intended consent.

Mitigation: Keep profile reading, parent-visible dashboards, reminder queueing, and saving plans off unless each is explicitly authorized; honor privacy controls and guardian requirements.

Risk: Mainland-China-specific crisis referral details may be unsuitable in other regions.

Mitigation: Confirm the student's region and localize referral information before deploying outside mainland China.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-plan)
- [Study plan templates](artifact/references/plan-templates.md)
- [Grade-band guidance](artifact/shared/grade-bands.md)
- [Crisis referral guidance](artifact/shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language study schedules, progress summaries, and optional printable family dashboards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Upper-primary plans cover one week; older students can receive 30-day plans. Profile use, family sharing, reminders, and plan storage require separate consent.]

## Skill Version(s):

2.9.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
