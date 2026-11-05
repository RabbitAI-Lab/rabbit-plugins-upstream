## Description:

Coordinates consent-based learning reminders by combining queued review and task items into daily summaries, with controls for timing, pausing, and sharing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

Students and their parents or teachers use the skill to set, review, pause, or adjust learning reminders for spaced review and planned tasks. It requires explicit consent before creating reminders, and primary-school students use it with an adult present.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reminder scheduling, storage, and privacy controls vary by host platform, and connected learning skills may share reminder data.

Mitigation: Choose reminder times and sharing permissions explicitly, and review the connected learning skills and host controls before use.

Risk: The release guidance notes that the skill may generate practice questions despite its scheduling-only description.

Mitigation: Check generated questions before using them and review the connected learning skill responsible for their content.

Risk: Younger students may need adult support when using learning reminders.

Mitigation: Have a parent or teacher present for primary-school use, as specified in the skill guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-im-reminder)
- [Interval review schedule](references/ebbinghaus-schedule.md)
- [Reminder handoff schema](shared/handover-protocol.schema.json)
- [Grade-band quiet hours](shared/grade-bands.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language reminder proposals, schedules, and queue summaries in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Conversational output; actual reminder timing depends on host scheduling support.]

## Skill Version(s):

2.12.5 (source: frontmatter; server release 2.12.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
