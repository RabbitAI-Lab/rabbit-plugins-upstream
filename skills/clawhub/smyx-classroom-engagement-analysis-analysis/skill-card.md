## Description:

Using a fixed classroom camera, this skill analyzes student facial expressions, estimates class-level engagement, identifies anonymous low-engagement seat positions, and provides heatmaps, alerts, and teacher-facing suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External educators and smart-classroom operators use this skill to analyze classroom camera images or videos for aggregate engagement trends, anonymous seat-level low-engagement cues, historical report lookup, and teaching suggestions. It is intended as a real-time teaching aid rather than a student identity, ranking, diagnosis, or performance evaluation system.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive classroom media is sent to cloud services.

Mitigation: Use only where school and parent consent, permitted data retention, and approved cloud processing terms are documented before installation.

Risk: Stored user credentials or reused accounts may have insufficient scoping and retention controls.

Mitigation: Confirm account and token handling, report ownership, credential rotation, and access boundaries before enabling analysis or history lookup.

Risk: Cloud report history and exported report links may expose sensitive classroom analysis results.

Mitigation: Restrict report access to approved staff and verify who can view historical reports and exported links.

Risk: Arbitrary public video URLs may introduce privacy and access-control issues.

Mitigation: Use approved classroom media sources and avoid untrusted public URLs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-classroom-engagement-analysis-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown summaries and JSON-style analysis reports with report links, alerts, heatmap references, and teacher-facing suggestions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include class-level engagement scores, anonymous seat coordinates, trend comparisons, historical report tables, and cloud report export links.]

## Skill Version(s):

1.0.7 (source: server release evidence; artifact frontmatter says 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
