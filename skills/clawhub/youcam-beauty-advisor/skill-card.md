## Description:

Recommends makeup looks from a user's selfie and provides a virtual try-on preview using YouCam AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcam-api](https://clawhub.ai/user/youcam-api)

### License/Terms of Use:

MIT-0

## Use Case:

People seeking personalized makeup suggestions can analyze a selfie, choose a full look or custom effects, and preview the result before applying makeup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selfies are uploaded to Perfect Corp/YouCam for analysis and makeup previews.

Mitigation: Get the user's informed agreement before submitting a selfie to the service.

Risk: Analysis and preview requests can consume API credits.

Mitigation: Show the credit cost and ask the user to choose an option before running it; check the existing task status rather than starting it again.

Risk: The YouCam API key grants access to the user's account.

Mitigation: Keep the key private and prefer the YOUCAM_API_KEY environment variable to a credentials file.

Risk: A generated makeup preview may not match actual results.

Mitigation: Label the preview as AI-generated and explain that products, skin, and lighting can change the outcome.

## Reference(s):

- [YouCam Beauty Advisor release](https://clawhub.ai/youcam-api/skills/youcam-beauty-advisor)
- [Beauty Advisor recommendation guide](references/guide.md)
- [Perfect Corp facial attribute analysis](https://docs.perfectcorp.com/reference/ai_face_analyzer.md)
- [Perfect Corp skin tone analysis](https://docs.perfectcorp.com/reference/ai_skin_tone_analysis.md)
- [Perfect Corp custom makeup try-on](https://docs.perfectcorp.com/reference/makeup_vto.md)
- [Perfect Corp full-look try-on](https://docs.perfectcorp.com/reference/ai_look_vto.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Image URL]

**Output Format:** [Markdown with a virtual try-on image URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Explains the recommendation and notes that the AI-generated preview may differ from real-world results.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
