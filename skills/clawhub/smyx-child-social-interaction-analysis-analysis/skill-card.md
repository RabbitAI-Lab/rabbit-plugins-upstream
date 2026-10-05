## Description:

Analyzes group video from kindergartens and early-education settings to summarize children's social interaction frequency, duration, and patterns in reports and heatmaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and early-education staff use the skill to review video-based counts and durations of interactions between children, identify children who may need additional attention, and retrieve historical reports. Results are educational aids, not developmental or medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's videos and social-interaction reports are sent to external services.

Mitigation: Obtain guardian and institution consent before use, and verify the services' retention and deletion practices.

Risk: Automatic identity reuse and locally stored tokens may expose sensitive reports.

Mitigation: Restrict access to historical reports and exports, and protect the workspace data directory as sensitive.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-child-social-interaction-analysis-analysis)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Markdown, JSON]

**Output Format:** [Text or JSON analysis reports; Markdown tables and links for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include per-child interaction counts, durations, alerts, and heatmap or report links.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
