## Description:

Monitors fixed-camera footage at a home entrance or balcony door to count a child's indoor/outdoor transitions, estimate daily outdoor duration, and produce structured reminders when the configured activity target is not met.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze home entrance or balcony-door video, summarize a child's outdoor-session counts and durations, and generate parent-facing activity reminders. It is intended for visual activity statistics and friendly reminders, not medical diagnosis or medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process sensitive video of children and home entrances.

Mitigation: Use it only with explicit guardian consent, confirm the video source is appropriate, and define retention and deletion expectations before analysis.

Risk: Analysis may upload files or URLs and query cloud-hosted historical reports.

Mitigation: Confirm the configured service endpoints are trusted and approved before running analysis or history queries.

Risk: The skill may silently manage an identity value and persist tokens locally.

Mitigation: Review local credential storage and account-linking behavior before installation, and clear stored tokens when the skill is no longer needed.

Risk: Outdoor duration is inferred from door or balcony transitions and may not equal true exercise or time outdoors.

Mitigation: Treat the report as visual activity statistics and combine it with caregiver judgment; do not use it for medical diagnosis or medical advice.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-child-outdoor-activity-monitor-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Child Outdoor Activity Monitoring API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-style structured analysis reports with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include activity metrics, alert type and level, recommendations, report links, or a Markdown table of historical reports.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata; artifact frontmatter lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
