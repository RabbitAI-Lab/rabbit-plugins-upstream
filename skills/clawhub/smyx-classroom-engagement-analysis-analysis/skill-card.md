## Description:

Analyzes classroom video to provide class-level engagement scores, seat-level alerts, heatmaps, and teaching suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and school administrators use classroom video to review aggregate engagement trends and receive real-time teaching prompts. The skill can also retrieve past analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Classroom video of minors and derived reports are sent to a cloud service and may be retained.

Mitigation: Require school or administrator approval, explicit consent, and a documented retention and deletion policy before use.

Risk: The local workspace may retain account identifiers and access tokens despite anonymity-focused descriptions.

Mitigation: Treat local workspace data as sensitive; restrict access and securely remove stored credentials and reports when no longer needed.

Risk: Seat-level engagement estimates can mischaracterize students or be misused for individual evaluation.

Mitigation: Use results only as teacher-facing classroom prompts; do not rank, discipline, or individually evaluate students.

## Reference(s):

- [Classroom engagement API documentation](references/api_doc.md)
- [Published ClawHub skill](https://clawhub.ai/18072937735/skills/smyx-classroom-engagement-analysis-analysis)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis reports, report links, and Markdown history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes class engagement scores, seat-level alerts, heatmaps, and teaching suggestions; reports may persist in the cloud.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
