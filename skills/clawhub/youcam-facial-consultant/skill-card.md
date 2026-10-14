## Description:

Analyzes a single selfie with YouCam to report skin and facial-feature colors, feature shapes, and approximate facial proportions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcam-api](https://clawhub.ai/user/youcam-api)

### License/Terms of Use:

MIT-0

## Use Case:

People seeking a color and facial-attribute reference can submit a selfie for a readable report on skin, eye, eyebrow, lip, and hair colors, feature shapes, and approximate facial proportions. This is not a medical or cosmetic-surgery assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A selfie is sent to Perfect Corp/YouCam for facial analysis, with privacy and retention disclosures not fully specified.

Mitigation: Get informed consent before uploading a selfie; review the provider's privacy and retention terms before use.

Risk: The API schema includes age and gender analysis beyond the stated skin tone and facial-attribute purpose.

Mitigation: Limit requests to the documented skin tone and facial attributes; do not request age or gender fields.

Risk: A YouCam API key is managed locally.

Mitigation: Keep the key private and avoid sharing or committing credential files.

## Reference(s):

- [Facial Consultant interpretation guide](references/guide.md)
- [YouCam skin tone analysis API](https://docs.perfectcorp.com/reference/ai_skin_tone_analysis.md)
- [YouCam face attributes and ratio analyzer API](https://docs.perfectcorp.com/reference/ai_face_analyzer.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Readable report with color palette, feature summary, facial proportions, and disclaimer]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports only returned attributes; labels proportions approximate and omits missing values.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
