## Description:

把独立教师分散在课表、学员卡、作业、家长沟通和课时包里的信息，只读聚合成一张可执行的日工作台。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to aggregate lesson schedule, student cards, homework, parent communication, course package, and progress evidence into a daily action dashboard. It helps prioritize today's classes, follow-ups, risk signals, renewal checkpoints, and the three most important actions without writing back to the workspace.

### Deployment Geography for Use:

Mainland China; localize emergency contacts, curriculum assumptions, and consent/legal rules before deployment elsewhere.

## Known Risks and Mitigations:

Risk: Dashboard outputs and exports can include minors' learning records and family communication context.

Mitigation: Install only where the teacher is authorized to access the student workspace, treat exports as sensitive, and use aliases instead of real student names.

Risk: Emergency contacts, curriculum assumptions, and consent rules are designed around mainland China defaults.

Mitigation: Localize crisis referral channels, curriculum expectations, and consent/legal requirements before using the skill in another region.

Risk: Risk flags or renewal priorities may be misleading when workspace records are missing, stale, or incomplete.

Mitigation: Base every flag on visible field values, show the supporting evidence, and require teacher confirmation before any follow-up action outside the dashboard.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-solo-dashboard)
- [Daily dashboard block templates](references/daily-dashboard-block-templates.md)
- [Daily dashboard full sample](references/daily-dashboard-full-sample.md)
- [Dashboard template](references/dashboard-template.md)
- [Solo teacher workspace schema](shared/solo-teacher-workspace.schema.json)
- [Platform conventions](shared/platform-conventions.md)
- [Crisis exception protocol](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown daily dashboard with seven structured sections and prioritized action items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only aggregation; does not write records, send parent messages, or execute external system actions.]

## Skill Version(s):

2.1.12 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
