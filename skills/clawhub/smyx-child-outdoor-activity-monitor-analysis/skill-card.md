## Description:

Analyzes fixed-camera footage of children entering and leaving a home or balcony to estimate daily outdoor time and provide activity reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and caregivers use fixed-camera videos or URLs to review a child's estimated outdoor time, activity reminders, and past reports. Results are visual estimates, not medical diagnoses or direct measurements of exercise.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child and home entrance footage or video URLs are sent to LifeEmergence cloud services.

Mitigation: Get guardian and household consent, minimize clips, and confirm the service's retention and deletion practices before use.

Risk: Reports are associated with a local or automatically created cloud-linked identity and token.

Mitigation: Review account and token handling, restrict access to reports, and use the service only when that identity linkage is acceptable.

Risk: Doorway observations may be mistaken for actual exercise or used as health assessments.

Mitigation: Treat durations as visual estimates and reminders, not medical advice or measurements of exercise.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-child-outdoor-activity-monitor-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Text or Markdown analysis reports and report links; optionally saved to a file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include estimated outdoor duration, exit and return events, reminders, and cloud report history.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
