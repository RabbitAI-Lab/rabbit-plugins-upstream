## Description:

Creates a read-only daily dashboard of an independent teacher's lessons, student follow-ups, homework, parent communications, and lesson packages, with evidence-based priorities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers with authorized access to student records use this skill to review a seven-section daily workspace, identify follow-ups from recorded facts, and prioritize three actions. It does not update records or contact parents on the teacher's behalf.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Student records and full workspace exports may disclose sensitive information.

Mitigation: Limit installation and access to authorized teachers or operators; handle dashboards and exports as sensitive records.

Risk: Crisis contacts, curriculum, and privacy defaults are specific to Mainland China.

Mitigation: Localize those defaults and verify local requirements before use elsewhere.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-solo-dashboard)
- [Daily dashboard block templates](artifact/references/daily-dashboard-block-templates.md)
- [Daily dashboard example](artifact/references/daily-dashboard-full-sample.md)
- [Teacher workspace schema](artifact/shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown daily dashboard or text workspace export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Seven dashboard sections, record-based risk flags, and three prioritized actions; read-only.]

## Skill Version(s):

2.10.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
