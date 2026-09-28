## Description:

Creates practical 30-day study plans for Chinese-speaking secondary students and weekly plans for upper-primary students, then helps adjust tasks based on progress.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking students in upper-primary, middle, and high school use this skill to turn learning goals and exam dates into manageable study schedules. Upper-primary students use a weekly version with an adult present; optional learning-profile access, parent-facing boards, and reminders require separate consent.

### Deployment Geography for Use:

Mainland China; use elsewhere only after localizing student safeguards and crisis referrals.

## Known Risks and Mitigations:

Risk: Access to minors' learning profiles or sharing task boards with parents without appropriate consent.

Mitigation: Keep profile access and parent sharing off by default; require separate, explicit student consent and guardian consent where age rules require it.

Risk: Unwanted reminders or changes to a student's stored study plan.

Mitigation: Require explicit consent before adding tasks to the reminder queue, and write a plan back only after a separate request to save it.

Risk: Mainland China-specific safeguarding and crisis referrals may not fit other regions.

Mitigation: Limit deployment to Chinese-speaking mainland China K-12 settings unless student safeguards and referral resources have been localized.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-plan)
- [Study-plan templates](references/plan-templates.md)
- [Grade-band guidance](shared/grade-bands.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language study schedules and optional parent-facing task boards in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Upper-primary plans cover one week; middle- and high-school plans cover 30 days.]

## Skill Version(s):

2.7.1 (source: server-resolved release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
