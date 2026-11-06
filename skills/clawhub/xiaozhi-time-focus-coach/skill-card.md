## Description:

帮助学生记录学习时间、分析高效时段和分心规律，并通过番茄钟安排专注时段。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students use this skill to log study time, review focus patterns, and plan focused work sessions. Timing starts only after the task, duration, and immediate start are confirmed; long-term storage, reminders, and cross-skill sharing are separate opt-in features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Guardian approval requirements for younger students' sharing and reminders are inconsistent.

Mitigation: Keep sharing and reminders disabled until guardian approval is consistently required and checked for each feature.

Risk: The separate profile-storage and reminder services are not included, so their runtime behavior is not established by this package.

Mitigation: Review those services before enabling long-term profile storage or queued reminders.

Risk: A focus timer could start before the student has clearly confirmed what to do, for how long, and whether to start now.

Mitigation: Confirm the task, duration, and immediate start before timing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-time-focus-coach)
- [Pomodoro state machine](artifact/references/pomodoro-statemachine.md)
- [Focus archive template](artifact/references/focus-archives-template.md)
- [Grade-band guidance](artifact/shared/grade-bands.md)
- [Platform conventions](artifact/shared/platform-conventions.md)
- [Crisis response guidance](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Conversational text with structured Markdown summaries when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Study-time summaries and focus-session guidance; cross-session conclusions depend on available, consented records.]

## Skill Version(s):

2.12.6 (source: release evidence, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
