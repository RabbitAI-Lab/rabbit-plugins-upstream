## Description:

Analyzes fixed classroom camera images or video to summarize facial-expression-based classroom engagement, class-level scores, anonymous low-engagement seat coordinates, heatmaps, alerts, and teacher-facing suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers, school operators, and smart-classroom developers use this skill to analyze classroom video or image inputs and receive aggregate engagement metrics, anonymous seat-level prompts, report links, and instructional suggestions. It is intended as teaching support, not as student identity recognition, student ranking, diagnosis, or performance evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student classroom video is uploaded to a cloud API for analysis.

Mitigation: Confirm the API operator, storage location, retention period, access controls, and school plus parent consent before using the skill in any child-facing setting.

Risk: Historical reports and report export links may remain accessible through cloud services.

Mitigation: Limit report access to authorized staff, define deletion and retention procedures, and verify that report links do not expose identifiable student data.

Risk: The skill silently creates or reuses local account credentials and tokens.

Mitigation: Run it in an isolated workspace, inspect and protect local credential storage, and remove local tokens and generated account data after use when they are no longer needed.

Risk: Facial-expression and posture signals can be misread as low engagement or confusion.

Mitigation: Use outputs only as aggregate teaching support and require human review before acting on seat-level prompts or classroom interventions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-classroom-engagement-analysis-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Classroom Engagement API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown and JSON-formatted text, with optional saved output files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include class engagement scores, emotion distributions, anonymous seat coordinates, heatmap image URLs, alert levels, teacher suggestions, and historical report listings.]

## Skill Version(s):

1.0.10 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
