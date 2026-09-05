## Description:

IM智能提醒 coordinates consented study reminders by accepting queued review and task items from other Xiaozhi skills, merging them into a daily summary, and sending only explicitly requested reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students, guardians, and learning agents use this skill to schedule, pause, inspect, and merge study reminders for spaced review, error review, planned tasks, exploration tasks, and daily confirmations. It is intended for consent-based K12 learning workflows where reminders must respect age band, quiet hours, and cross-skill sharing permissions.

### Deployment Geography for Use:

Mainland China; localize crisis contacts, curriculum assumptions, and minor-consent rules before use elsewhere.

## Known Risks and Mitigations:

Risk: Minors could receive scheduled reminders without age-band-aware guardian or joint consent.

Mitigation: Review consent handling before installation and require the appropriate student, guardian, or joint consent before enabling reminders.

Risk: Cross-skill reminder enqueue and sync messages may validate the wrong sender or recipient if the routing contract is inconsistent.

Mitigation: Fix and test the handover schema so each reminder_enqueue and reminder_sync workflow validates the correct sender, recipient, consent snapshot, and payload.

Risk: Deployments outside mainland China may use unsuitable crisis contacts, curriculum assumptions, or minor-consent defaults.

Mitigation: Localize crisis referrals, education assumptions, and consent requirements before making the skill available in another region.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-im-reminder)
- [Ebbinghaus Spaced Review Schedule](artifact/references/ebbinghaus-schedule.md)
- [Reminder Budget and Consent Vocabulary](artifact/shared/vocab.md)
- [Grade Bands and Quiet Hours](artifact/shared/grade-bands.md)
- [Handover Protocol Schema](artifact/shared/handover-protocol.schema.json)
- [Reminder Enqueue Example](artifact/shared/reminder-enqueue.example.json)
- [Crisis Referral Protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Configuration, Guidance]

**Output Format:** [Markdown-style reminder messages, queue summaries, consent prompts, and JSON handoff examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires platform support for scheduled reminders, persistent memory, and current-date awareness; falls back to session-entry catch-up when scheduled push is unavailable.]

## Skill Version(s):

2.1.6 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
