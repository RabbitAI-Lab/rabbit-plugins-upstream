## Description:

Creates a read-only daily dashboard for independent teachers, combining lesson schedules, student follow-ups, parent communication, and remaining lesson credits into prioritized actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to review today's lessons and student follow-ups, identify evidence-backed concerns, and choose their three most important actions without changing student records or sending messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A dashboard or text export may expose minors' educational records or family details.

Mitigation: Check consent before using real records, keep exports private, use student aliases, and omit sensitive personal details.

Risk: Incomplete or stale records may produce misleading priorities or lesson-credit alerts.

Mitigation: Review the underlying dated records and pending credit confirmations before acting; the teacher remains responsible for decisions.

Risk: Emergency and education-related guidance may not fit locations outside mainland China.

Mitigation: Localize emergency contacts and applicable legal guidance before use outside mainland China.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-solo-dashboard)
- [Daily dashboard template](artifact/references/dashboard-template.md)
- [Seven dashboard block templates](artifact/references/daily-dashboard-block-templates.md)
- [Daily dashboard example](artifact/references/daily-dashboard-full-sample.md)
- [Teacher workspace data schema](artifact/shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown daily dashboard with seven sections and three prioritized actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; uses student aliases and cites record-based reasons for attention flags.]

## Skill Version(s):

2.11.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
