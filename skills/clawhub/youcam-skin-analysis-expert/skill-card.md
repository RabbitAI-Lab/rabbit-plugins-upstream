## Description:

Analyzes a user-provided selfie with YouCam to produce a readable skin-condition report with scores and skin type.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcam-api](https://clawhub.ai/user/youcam-api)

### License/Terms of Use:

MIT-0

## Use Case:

People seeking a cosmetic skin assessment use this skill to identify their lowest- and highest-scoring concerns and receive a readable report with skincare guidance. It requires a selfie and a YouCam API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A selfie and skin-analysis results are shared with YouCam/Perfect Corp.

Mitigation: Obtain the user's consent and avoid permanent public image URLs.

Risk: The YouCam API key grants access to a paid service.

Mitigation: Use the environment variable for the key and keep it out of shared files and reports.

Risk: Analysis consumes API credits, and repeating a pending run may incur another charge.

Mitigation: Review the credit cost before running and check the existing task status instead of rerunning it.

Risk: Skin scores may be mistaken for medical advice or distorted by photo quality.

Mitigation: Present results as non-diagnostic, note photo-quality limits, and recommend a dermatologist for skin-health concerns.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/youcam-api/skills/youcam-skin-analysis-expert)
- [YouCam AI Skin Analysis API documentation](https://docs.perfectcorp.com/reference/ai_skin_analysis.md)
- [Skin analysis interpretation](references/interpretation.md)
- [Skin analysis report format](references/output-format.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report with skin scores, a concern table, skincare guidance, and analysis images when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes skin type, three lowest- and three highest-scoring concerns, and a non-medical disclaimer.]

## Skill Version(s):

1.1.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
