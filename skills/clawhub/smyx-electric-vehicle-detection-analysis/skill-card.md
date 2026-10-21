## Description:

Analyzes images and videos for e-bikes and electric motorcycles in restricted areas, reporting suspected parking or driving violations and management alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Security teams and site managers use the skill to review surveillance images or videos for electric vehicles in restricted areas, receive violation counts and alerts, and consult previous detection reports. Suspected violations require human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted surveillance images, videos, and report metadata are sent to a cloud service.

Mitigation: Use only with approved media and a trusted cloud service; confirm uploads with the user first.

Risk: A persistent fallback identity and token cache can mix report histories across users in shared workspaces.

Mitigation: Avoid shared workspaces until identity isolation is fixed; require scoped per-user credentials and confirm history queries.

Risk: Automated violation detections may be mistaken for final determinations.

Mitigation: Have a person verify suspected violations before taking action.

## Reference(s):

- [Electric vehicle detection API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [ClawHub release listing](https://clawhub.ai/18072937735/skills/smyx-electric-vehicle-detection-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Detection report or JSON results; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes vehicle and violation counts, severity alerts, management suggestions, and report links when available]

## Skill Version(s):

9.9.19 (source: ClawHub release metadata; bundled skill frontmatter: 1.0.23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
