## Description:

Creates a read-only daily dashboard for independent teachers, bringing together schedules, student progress, homework, parent follow-ups, and lesson packages into seven actionable sections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent K–12 teachers use this skill to review their daily teaching workload, identify students needing follow-up from recorded evidence, and prioritize three next actions without changing workspace records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dashboard may summarize sensitive student operational data.

Mitigation: Use student aliases, keep consent fields current, and review who can access the dashboard.

Risk: A vague personal-planning request may load the teacher workspace unintentionally.

Mitigation: Invoke the skill only when a teacher-workspace dashboard is intended; clarify ambiguous requests first.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-solo-dashboard)
- [Daily dashboard template](artifact/references/dashboard-template.md)
- [Seven dashboard block templates](artifact/references/daily-dashboard-block-templates.md)
- [Daily dashboard example](artifact/references/daily-dashboard-full-sample.md)
- [Teacher workspace data schema](artifact/shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown daily dashboard]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Seven sections with evidence-based risk flags and three prioritized actions; read-only.]

## Skill Version(s):

2.4.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
