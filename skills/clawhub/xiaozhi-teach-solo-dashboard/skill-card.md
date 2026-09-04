## Description:

把独立教师分散在课表、学员卡、作业、家长沟通和课时包里的信息，只读聚合成一张可执行的日工作台。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to turn daily schedule, student-card, homework, parent-communication, course-package, and progress evidence into a read-only daily work dashboard. It highlights field-based student risks, pending feedback, renewal attention points, and the three most important actions for the day.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student workspace records may include sensitive education, communication, and course-package information.

Mitigation: Install only for consented and pseudonymized independent-teacher workspaces, and restrict dashboard access to authorized teachers.

Risk: Crisis or self-harm signals require escalation beyond a learning dashboard.

Mitigation: Confirm local emergency and crisis resources before use, and follow the bundled crisis referral protocol when crisis signals appear.

Risk: Privacy requests such as delete, export, or correction may affect student records.

Mitigation: Clarify how those requests are authenticated and executed before deployment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-solo-dashboard)
- [Dashboard template](references/dashboard-template.md)
- [Daily dashboard block templates](references/daily-dashboard-block-templates.md)
- [Daily dashboard full sample](references/daily-dashboard-full-sample.md)
- [Solo teacher workspace schema](shared/solo-teacher-workspace.schema.json)
- [Crisis exception protocol](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Chinese-language Markdown dashboard with seven sections and prioritized action items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only aggregation using pseudonymous student aliases and field-based risk signals.]

## Skill Version(s):

2.1.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
