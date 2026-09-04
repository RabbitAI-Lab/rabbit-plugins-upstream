## Description:

IM智能提醒 consolidates review, mistake-retest, study-plan, and exploration reminders from other Xiaozhi skills into one consent-based daily learning reminder summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students, guardians, and education agents use this skill to schedule opt-in Chinese-language study reminders, merge queued learning tasks into a daily summary, and manage reminder controls such as pause, adjust, delete, and export.

### Deployment Geography for Use:

Global, with localization review for country-specific crisis and emergency guidance.

## Known Risks and Mitigations:

Risk: Scheduled reminders could be enabled for students without clear opt-in or guardian consent.

Mitigation: Require explicit reminder consent before scheduling, and confirm guardian consent for younger students before broad use.

Risk: Reminder scheduling and learning-profile memory can expose sensitive study habits or cross-skill context.

Mitigation: Share only the minimum fields needed for reminder enqueue and sync, and keep view, pause, delete, export, and sharing controls available.

Risk: Crisis and emergency guidance may rely on Chinese-language or China-specific assumptions.

Mitigation: Localize crisis referral and emergency instructions for the deployment country before using the skill outside its intended locale.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/qizhitang/skills/xiaozhi-im-reminder)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Ebbinghaus spaced-review schedule](artifact/references/ebbinghaus-schedule.md)
- [Reminder budget and vocabulary contract](artifact/shared/vocab.md)
- [Grade-band reminder windows](artifact/shared/grade-bands.md)
- [Reminder handover protocol schema](artifact/shared/handover-protocol.schema.json)
- [AI-generated item self-check protocol](artifact/shared/ai-item-check.md)
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/schema)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Chinese-language reminder text, Markdown queue summaries, and JSON handover payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reminder outputs are consent-gated, budgeted to daily summaries plus limited immediate reminders, and may degrade to in-session follow-up when scheduled push capability is unavailable.]

## Skill Version(s):

2.1.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
