## Description:

把学习目标拆成可执行的 30 天方案（小学高段用周计划版），并在学生开启后跟进执行偏差。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in upper primary, middle school, and high school use this skill to turn learning goals, weak-area summaries, available study time, and exam timelines into practical weekly or 30-day study plans. With separate consent, it can also help track execution drift, prepare parent-visible task dashboards, and queue reminder handoffs.

### Deployment Geography for Use:

China Mainland by default; other regions require localized emergency and youth-support guidance before deployment.

## Known Risks and Mitigations:

Risk: Student learning profile summaries could be used without the separate consent expected by the release.

Mitigation: Keep profile sharing off by default, require explicit consent before reading weak-area, rhythm, and completion summaries, and preserve view, correction, deletion, pause, and sharing controls.

Risk: Parent-visible dashboards could disclose more than the student intended.

Mitigation: Generate parent-visible content only after parent-sharing consent and speaker checks, omit emotion and diagnostic interpretations, and honor student vetoes for middle and high school users.

Risk: Crisis or self-harm signals could be minimized as ordinary study stress or routed with region-inappropriate support contacts.

Mitigation: Stop normal planning flows on crisis signals, direct the student to trusted adults and local emergency support, and localize non-China help channels before deployment.

Risk: Reminder behavior could over-notify students or imply that this skill sends reminders itself.

Mitigation: Use reminder handoff entries only after reminder consent, rely on the platform reminder queue, and enforce reminder budgets and pause controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-plan)
- [Plan templates](artifact/references/plan-templates.md)
- [Grade-band parameters](artifact/shared/grade-bands.md)
- [Shared vocabulary and consent fields](artifact/shared/vocab.md)
- [Platform conventions and reminder handoff](artifact/shared/platform-conventions.md)
- [Crisis exception](artifact/shared/crisis-exception.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Chinese Markdown/plain text with optional structured reminder handoff entries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include consent-gated parent-visible dashboard content and localized crisis-referral guidance.]

## Skill Version(s):

2.1.12 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
