## Description:

Turns a student's weekly learning records into an evidence-based review and a focused next step, with guided self-reflection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking students use this skill to review a week's learning evidence, identify progress and sticking points, and choose one priority for next week. A family-facing version requires the student's consent.

### Deployment Geography for Use:

Mainland China; localize curriculum, consent rules, and crisis referrals before use elsewhere.

## Known Risks and Mitigations:

Risk: Weekly reviews and family summaries may expose a student's learning or emotional information.

Mitigation: Confirm the student's consent for sharing and profile updates; omit emotional details from family summaries without separate permission.

Risk: Reminder scheduling and learning-profile updates may persist information beyond the current review.

Mitigation: Request consent for each handoff, honor pause and deletion requests, and do not enqueue reminders without authorization.

Risk: Curriculum, consent expectations, and crisis contacts may not fit users outside Mainland China.

Mitigation: Localize these safeguards before deployment elsewhere and use region-appropriate crisis referrals.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-weekly-review)
- [Weekly review report templates](references/review-report-template.md)
- [Grade-band guidance](shared/grade-bands.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language weekly review and self-reflection prompts; optional consent-based family summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can propose a consent-based learning-profile summary and weekly reminder; does not generate monthly reports.]

## Skill Version(s):

2.7.1 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
