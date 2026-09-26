## Description:

Turns a student's weekly learning records into an evidence-based review with one next-step priority and guided self-reflection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking K–12 students use this skill to review a week of learning, identify evidence of progress and difficulties, and choose one priority for the next week. With the student's consent, it can prepare a family-facing version and share a growth summary or reminder.

### Deployment Geography for Use:

Mainland China (Chinese-language K–12 context)

## Known Risks and Mitigations:

Risk: A child's learning or emotional information could be shared or retained against their wishes.

Mitigation: Confirm consent for memory, cross-skill sharing, family reports, and reminders; honor pause, correction, deletion, and sharing controls.

Risk: Curriculum assumptions, minor-data consent practices, and crisis contacts may be inappropriate outside Mainland China.

Mitigation: Localize language, curriculum, consent rules, and crisis contacts before deployment elsewhere; confirm location before suggesting local help.

Risk: Sparse weekly records can make progress metrics and conclusions misleading.

Mitigation: Label limited evidence and avoid unsupported historical counts or completion rates.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-weekly-review)
- [Weekly review report templates](references/review-report-template.md)
- [Privacy and consent conventions](shared/vocab.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [Handover protocol schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown weekly review for the student; optional consented family summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a focused next-week action; growth-summary sharing and review reminders require consent.]

## Skill Version(s):

2.6.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
