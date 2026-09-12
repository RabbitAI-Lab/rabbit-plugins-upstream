## Description:

IM智能提醒 consolidates student-approved study reminders from other Xiaozhi skills into a daily summary, handling scheduling, quiet hours, consent checks, pauses, and response updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, guardians, and education agents use this skill to schedule consent-based review, error-retest, plan, exploration, and daily-confirmation reminders. It is intended to reduce interruption by merging due learning items into a small number of user-controlled reminders.

### Deployment Geography for Use:

China Mainland by default; localize consent rules, curriculum assumptions, quiet hours, and crisis contacts before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill can store and send student reminders in deployments involving minors.

Mitigation: Install only where the platform verifies the authenticated user, age band, consenting principal, and current reminder consent before creating or sending reminders.

Risk: Cross-skill reminder intake can expose or reuse student learning data beyond the user's intent.

Mitigation: Require explicit cross-skill sharing consent and pass only the minimum reminder fields needed for scheduling and delivery.

Risk: Reminder content from other skills may contain untrusted text.

Mitigation: Treat reminder content as display text with escaping, length limits, and review controls before notification delivery.

Risk: Default safety contacts, curriculum assumptions, and quiet-hour guidance are designed for a Chinese K12 context.

Mitigation: Localize emergency guidance, consent requirements, school-calendar assumptions, and reminder windows before deployment outside that context.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-im-reminder)
- [Ebbinghaus review schedule](artifact/references/ebbinghaus-schedule.md)
- [Grade bands and quiet-hour limits](artifact/shared/grade-bands.md)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)
- [Platform conventions and degradation paths](artifact/shared/platform-conventions.md)
- [Reminder enqueue example](artifact/shared/reminder-enqueue.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Concise chat text or Markdown for reminder summaries, plus structured reminder queue and status fields when used through the handover protocol.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Depends on platform time, date, reminder, and memory capabilities; without timer support, it degrades to due-item recap when the user next enters a session.]

## Skill Version(s):

2.1.12 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
