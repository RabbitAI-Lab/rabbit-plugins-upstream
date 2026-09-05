## Description:

Creates consent-gated weekly or 30-day study plans for upper-primary, middle-school, and high-school students from stated goals and optional learning-profile summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, guardians, and education operators use this skill to turn a student's goals, grade band, available time, and optional learning-profile summaries into practical study schedules. It is tailored to Mainland China Chinese K12 assumptions and should be localized before use in other regions.

### Deployment Geography for Use:

Mainland China by default; other regions only after localizing curriculum assumptions, minor-consent requirements, and crisis-referral resources.

## Known Risks and Mitigations:

Risk: The skill may save a child's plan data to a long-term learning profile without a clearly separate save-consent gate.

Mitigation: Require explicit consent before profile writes; honor delete, export, and do-not-remember controls; and default to current-session planning when consent is absent.

Risk: Mainland China K12 curriculum, consent, and crisis-referral assumptions may be inappropriate in other regions.

Mitigation: Localize curriculum mappings, minor-consent rules, and crisis-referral resources before deployment outside the intended setting.

Risk: Reminder tasks could be handed off to an unintended reminder service.

Mitigation: Verify reminder handoffs route only to the intended reminder service and only after reminder consent is present.

Risk: Parent-facing boards can disclose student progress or sensitive context.

Mitigation: Generate parent-visible output only after speaker identity and parent-sharing consent checks; omit emotion content unless separately consented, except for the crisis-safety override.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-plan)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Plan templates](artifact/references/plan-templates.md)
- [Grade-band parameters](artifact/shared/grade-bands.md)
- [Shared vocabulary and consent model](artifact/shared/vocab.md)
- [Crisis exception](artifact/shared/crisis-exception.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or plain text study plans, family board summaries, and structured reminder/profile handoff payloads when authorized.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are grade-band aware and should apply separate consent gates for profile access, parent-visible summaries, and reminder handoff.]

## Skill Version(s):

2.1.6 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
