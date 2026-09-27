## Description:

Creates a read-only daily dashboard for independent teachers, bringing together schedules, student records, homework, parent follow-ups, lesson balances, and three prioritized actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent K–12 teachers use this skill to review their daily teaching workload, identify students needing attention from recorded data, and prioritize three actions without changing records or contacting parents.

### Deployment Geography for Use:

Mainland China (localize language, grade conventions, crisis contacts, and privacy assumptions before use elsewhere)

## Known Risks and Mitigations:

Risk: Student information or parent-facing summaries could expose sensitive details without consent.

Mitigation: Use student aliases, omit sensitive family and medical details, and confirm workspace consent fields are enforced before sharing parent-facing content.

Risk: Mainland China grade conventions and crisis contacts may be inappropriate elsewhere.

Mitigation: Use only for Chinese-language Mainland China K–12 workflows unless language, grade conventions, crisis contacts, and privacy assumptions are localized.

Risk: Missing or incomplete teaching records can make student attention flags or priorities misleading.

Mitigation: Base flags on recorded field values, distinguish subjective judgments, and have the teacher review priorities before acting.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-solo-dashboard)
- [Daily dashboard template](references/dashboard-template.md)
- [Seven-block dashboard templates](references/daily-dashboard-block-templates.md)
- [Daily dashboard example](references/daily-dashboard-full-sample.md)
- [Teacher workspace schema](shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown daily dashboard with seven sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only summary with data-based student attention flags and three prioritized actions; no messages sent or records modified.]

## Skill Version(s):

2.7.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
