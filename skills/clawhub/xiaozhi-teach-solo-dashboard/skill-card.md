## Description:

Aggregates a solo teacher's schedule, student records, homework follow-up, parent communication, and course-package data into a read-only daily dashboard with risk flags and top priorities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External educators and agents use this skill to turn existing solo-teacher workspace records into a seven-section daily dashboard. It helps identify today's classes, preparation and feedback tasks, homework and parent-communication follow-up, course-package renewal points, and the three most important actions for the day.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads sensitive student records in a teacher workspace.

Mitigation: Install it only where the agent is authorized to read those records, keep outputs alias-only, and apply consent checks before any parent communication or cross-skill sharing.

Risk: Ambiguous teacher requests could expose or summarize more student data than intended.

Mitigation: Confirm ambiguous requests before loading the dashboard and summarize only the fields needed for the daily work plan.

Risk: Course-package and parent-communication guidance could be mistaken for permission to take action.

Mitigation: Keep the dashboard read-only and route record updates, message sending, and course confirmation to the appropriate skill or human action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-solo-dashboard)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Daily dashboard block templates](references/daily-dashboard-block-templates.md)
- [Daily dashboard full sample](references/daily-dashboard-full-sample.md)
- [Dashboard template](references/dashboard-template.md)
- [Solo teacher workspace schema](shared/solo-teacher-workspace.schema.json)
- [AI item check](shared/ai-item-check.md)
- [Crisis exception protocol](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown dashboard with structured sections and action guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only aggregation; does not send messages, update records, or confirm course-package changes.]

## Skill Version(s):

2.1.6 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
