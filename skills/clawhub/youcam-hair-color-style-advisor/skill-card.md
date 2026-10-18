## Description:

Recommends hairstyles and hair colors based on a user's face shape and skin tone, with optional AI-generated try-on previews through YouCam.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcam-api](https://clawhub.ai/user/youcam-api)

### License/Terms of Use:

MIT-0

## Use Case:

People seeking hairstyle or hair-color ideas can receive tailored recommendations and, if they choose, preview a new style or color using a selfie.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selfies or reference images are sent to Perfect Corp/YouCam for analysis and previews.

Mitigation: Obtain the user's agreement before sending images and use an environment variable for the API key when possible.

Risk: Generating previews and running analysis can consume paid API credits.

Mitigation: Check and explain credit costs, ask which actions the user wants, and obtain approval before paid tasks.

Risk: AI-generated previews may not match achievable salon results.

Mitigation: Label previews as reference only and recommend consulting a professional stylist for coloring.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/youcam-api/skills/youcam-hair-color-style-advisor)
- [Recommendation guide](references/guide.md)
- [YouCam facial analysis documentation](https://docs.perfectcorp.com/reference/ai_face_analyzer.md)
- [YouCam skin tone analysis documentation](https://docs.perfectcorp.com/reference/ai_skin_tone_analysis.md)
- [YouCam hairstyle documentation](https://docs.perfectcorp.com/reference/ai_hairstyle.md)
- [YouCam hair color documentation](https://docs.perfectcorp.com/reference/ai_hair_color.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with a preview image URL when generation is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Explains the recommendation and notes that AI previews may differ from real results.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
