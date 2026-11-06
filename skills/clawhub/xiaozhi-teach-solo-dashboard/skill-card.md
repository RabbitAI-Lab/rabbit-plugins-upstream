## Description:

Aggregates a solo teacher’s schedules, student records, assignments, parent communication, and lesson packages into a read-only daily dashboard with evidence-based follow-up priorities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to review classes, preparation, follow-ups, student risk signals, and remaining lesson credits in one daily dashboard. It summarizes authorized workspace records and suggests priorities for the teacher to review.

### Deployment Geography for Use:

China-focused; the skill documentation frames its training use around China-specific rules.

## Known Risks and Mitigations:

Risk: Student and guardian records may contain sensitive or identifying information.

Mitigation: Use aliases and authorized records, check consent before sharing, and review the platform’s storage and access settings.

Risk: Dashboard suggestions rely on the records available and need teacher review before action.

Mitigation: Confirm the underlying records and review each suggestion; this skill does not change records or send messages.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-solo-dashboard)
- [Seven-section dashboard templates](references/daily-dashboard-block-templates.md)
- [Full dashboard example](references/daily-dashboard-full-sample.md)
- [Solo teacher workspace schema](shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Guidance]

**Output Format:** [Markdown daily dashboard organized into seven sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only summary of available workspace records; missing records are identified, and suggested priorities include supporting evidence for teacher review.]

## Skill Version(s):

2.12.6 (source: ClawHub release metadata, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
