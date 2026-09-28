## Description:

Aggregates a solo teacher's schedules, student records, homework, parent communications, and lesson balances into a read-only daily dashboard with prioritized follow-ups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent K–12 teachers use this read-only skill to review a seven-part daily workspace, identify students needing follow-up using recorded evidence, and prioritize three actions. Changes to records and messages to parents remain with the teacher or other skills.

### Deployment Geography for Use:

Mainland China (Simplified-Chinese K–12 workflow); localize crisis resources before use elsewhere

## Known Risks and Mitigations:

Risk: The dashboard and optional text export can expose sensitive student, parent-communication, and lesson-package records.

Mitigation: Use only with appropriate consent, show student aliases where possible, and restrict access to and retention of exported text.

Risk: The default crisis guidance is tailored to Mainland China and may not fit other locations.

Mitigation: Confirm the intended location before deployment and localize emergency contacts for other regions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-solo-dashboard)
- [Daily dashboard template](artifact/references/dashboard-template.md)
- [Seven dashboard block templates](artifact/references/daily-dashboard-block-templates.md)
- [Daily dashboard example](artifact/references/daily-dashboard-full-sample.md)
- [Student workspace data schema](artifact/shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured daily dashboard and action list; text export on request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Seven read-only sections with evidence-based student flags and three prioritized tasks; no automatic parent messages or record updates.]

## Skill Version(s):

2.7.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
