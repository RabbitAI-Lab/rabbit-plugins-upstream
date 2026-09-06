## Description:

把独立教师分散在课表、学员卡、作业、家长沟通和课时包里的信息，只读聚合成一张可执行的日工作台。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill to turn lesson schedules, student cards, homework follow-ups, parent communication logs, course-package records, and progress evidence into a daily dashboard. It highlights today's lessons, preparation needs, follow-up work, student risk signals, renewal points, and the three most important actions without writing back to the workspace.

### Deployment Geography for Use:

Global; artifact guidance says the default Chinese K12 safety and curriculum assumptions are for Mainland China and should be localized before use elsewhere.

## Known Risks and Mitigations:

Risk: Dashboards or exported records may expose student workspace information to an unauthorized requester or an untrusted location.

Mitigation: Confirm the requester is the teacher or another authorized person, scope outputs to the needed student, date, or record type, use aliases instead of real names, and avoid moving exported text into untrusted chats or files.

Risk: Risk labels can become misleading when records are missing, dates are incomplete, or subjective impressions are mixed with field-based signals.

Mitigation: Base risk flags on documented field values, sort recent lesson evidence by date, say when records are unavailable, and clearly label any teacher-provided subjective judgment.

Risk: A dashboard suggestion could be mistaken for permission to send parent messages, change schedules, or confirm course-package deductions.

Mitigation: Keep the dashboard read-only and route parent communication, scheduling, homework, lesson-log, and renewal actions to the relevant skill for explicit teacher confirmation.

Risk: Student safety or crisis signals may appear while the dashboard is reading learning records.

Mitigation: Stop normal dashboard output for crisis signals, avoid recording sensitive details, direct the user to trusted adults and local emergency resources, and localize emergency contact guidance outside Mainland China.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-solo-dashboard)
- [Daily dashboard template](artifact/references/dashboard-template.md)
- [Daily dashboard block templates](artifact/references/daily-dashboard-block-templates.md)
- [Daily dashboard full sample](artifact/references/daily-dashboard-full-sample.md)
- [Solo teacher workspace schema](artifact/shared/solo-teacher-workspace.schema.json)
- [Platform conventions](artifact/shared/platform-conventions.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown daily dashboard with structured sections and concise action items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only output; uses student aliases, cites field-based evidence for risk flags, and routes write actions to other skills for teacher confirmation.]

## Skill Version(s):

2.1.10 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
