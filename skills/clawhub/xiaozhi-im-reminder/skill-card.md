## Description:

IM智能提醒 consolidates consented Chinese K12 study review, task, and follow-up reminders from other Xiaozhi skills into a daily summary and sends or queues reminders only when the student explicitly asks or authorizes them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, guardians, and learning-support agents use this skill to manage consented Chinese K12 study reminders, including spaced review, error-review follow-ups, planned study tasks, exploration tasks, and daily confirmations. It is intended to reduce reminder overload by merging due items into a limited daily summary and respecting pause, cancel, sharing, and quiet-hour controls.

### Deployment Geography for Use:

Default configuration is for mainland China Chinese K12 learning contexts; other regions require localized guardian-consent, data-sharing, and crisis-contact settings before use.

## Known Risks and Mitigations:

Risk: The skill handles reminders for minors in a China-focused K12 context.

Mitigation: Confirm reminder consent, guardian involvement for younger students, and local legal requirements before deployment, especially outside mainland China.

Risk: Reminder workflows can become intrusive or create pressure if they run without clear consent or limits.

Mitigation: Create reminders only after explicit student or guardian authorization, provide pause/cancel controls, cap reminders to the daily budget, and honor grade-band quiet hours.

Risk: Cross-skill reminder intake can expose more learning-profile data than needed.

Mitigation: Require cross-skill sharing and reminder-consent flags, accept only the minimum fields needed for the reminder, and avoid default synchronization back to other skills.

Risk: Crisis or safety disclosures can appear during learning conversations.

Mitigation: Stop the reminder flow, avoid diagnosis, prompt contact with trusted adults, and use localized emergency or crisis-contact guidance.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-im-reminder)
- [Ebbinghaus schedule reference](artifact/references/ebbinghaus-schedule.md)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)
- [Grade-band reminder windows](artifact/shared/grade-bands.md)
- [Crisis exception protocol](artifact/shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Configuration, Guidance]

**Output Format:** [Chinese conversational reminders, queue summaries, and structured reminder_enqueue/reminder_sync JSON guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires reminder consent; daily summaries are capped and quiet hours apply by grade band.]

## Skill Version(s):

2.3.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
