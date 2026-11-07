## Description:

Using a fixed classroom camera, the system analyzes students' facial expressions, calculates a class-level engagement score, and provides engagement heatmaps and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and education teams use classroom video to review group-level engagement patterns, notice possible confusion or low engagement, and adjust instruction. Results are intended as teaching support, not individual assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The no-analysis option fails, endpoint controls need review, and raw-video processing and retention are not clearly explained.

Mitigation: Use test footage until these controls are fixed. Before using student footage, confirm how raw video is processed, retained, and deleted.

Risk: Anonymous reports do not make uploaded student footage anonymous, and account credential safeguards are unclear.

Mitigation: Obtain the required school and parent consent, protect stored tokens, and verify safeguards before handling student footage.

## Reference(s):

- [API documentation](references/api_doc.md)
- [API error codes](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release](https://clawhub.ai/18072937735/skills/smyx-classroom-engagement-analysis-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown, Images]

**Output Format:** [Structured analysis results and reports, with suggestions, report links, and engagement heatmaps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Class-level engagement summaries and anonymous seat-coordinate alerts; the skill documentation says not to use results for student ranking or performance evaluation.]

## Skill Version(s):

1.0.16 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
