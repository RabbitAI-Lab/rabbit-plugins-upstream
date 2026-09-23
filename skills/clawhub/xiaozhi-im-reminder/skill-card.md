## Description:

IM智能提醒 consolidates consented K12 learning reminders for review, error retesting, plans, and exploration tasks into daily summaries with quiet-hour and pause controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent builders use this skill in Chinese K12 learning assistants to schedule, merge, and send authorized learning reminders. It is intended for consent-based reminder workflows that need daily budget limits, quiet hours, pause/delete controls, and limited cross-skill status sharing.

### Deployment Geography for Use:

Mainland China by default; other regions require localization of language, curriculum assumptions, legal consent defaults, and crisis-contact channels before use.

## Known Risks and Mitigations:

Risk: The skill is designed for Chinese K12 learning reminders and may be inappropriate if deployed in a different curriculum, language, legal-consent, or crisis-support context without localization.

Mitigation: Deploy only where the host platform can localize language, curriculum assumptions, consent defaults, guardian requirements, and regional crisis-contact channels.

Risk: Reminder workflows can become intrusive or unsafe if consent, quiet hours, or learner controls are not enforced.

Mitigation: Require explicit reminder consent, honor quiet-hour windows and daily reminder budgets, and expose pause, delete, adjust, export, and sharing controls.

Risk: Cross-skill reminder status sharing can expose student learning data beyond the minimum needed for the task.

Mitigation: Share only minimal reminder status or priority fields after explicit authorization, and avoid default synchronization of full learner profiles.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-im-reminder)
- [Ebbinghaus schedule reference](artifact/references/ebbinghaus-schedule.md)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)
- [Handover protocol schema URL](https://xiaozhi-skills.openclaw.dev/schemas/handover-protocol.schema.json)
- [Grade bands and quiet-hour table](artifact/shared/grade-bands.md)
- [Platform conventions](artifact/shared/platform-conventions.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [AI item check protocol](artifact/shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Chinese conversational reminder text, markdown queue summaries, and JSON reminder_enqueue/reminder_sync payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are constrained by explicit consent, guardian requirements where applicable, quiet hours, daily reminder budgets, pause/delete/export controls, and localized crisis-referral handling.]

## Skill Version(s):

2.2.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
