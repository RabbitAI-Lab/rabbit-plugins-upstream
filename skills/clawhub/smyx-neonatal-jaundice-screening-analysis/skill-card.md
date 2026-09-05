## Description:

Analyzes newborn face images or short videos to produce a visual jaundice risk hint based on sclera color and facial skin yellowness, with non-diagnostic guidance for follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, clinical support teams, and developers use this skill to pre-screen newborn face images or short videos for visual jaundice risk and to retrieve cloud-linked historical screening reports. The output is a preliminary risk hint and follow-up guidance, not a medical diagnosis or bilirubin measurement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive newborn images, videos, and account-linked report history through cloud services.

Mitigation: Use only where a guardian has explicitly consented to cloud processing, and apply appropriate access control, encryption, and retention practices for submitted media and reports.

Risk: The skill can create or reuse a local default identity and store API tokens in a workspace SQLite database.

Mitigation: Run it in an isolated workspace, restrict access to local storage, and remove local identity or token data when it is no longer needed.

Risk: Visual jaundice screening can be misleading under poor lighting, color casts, filters, occlusion, or unclear facial views.

Mitigation: Capture clear images in natural white light, treat inconclusive or medium/high risk outputs conservatively, and confirm concerns with professional bilirubin testing and clinical review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-neonatal-jaundice-screening-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface reference](references/api_doc.md)
- [Analysis API error reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown and JSON-style structured screening reports with risk level, confidence, recommended action, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include low, medium, high, or inconclusive jaundice-risk hints; historical report queries are returned from cloud-linked records.]

## Skill Version(s):

1.0.10 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
