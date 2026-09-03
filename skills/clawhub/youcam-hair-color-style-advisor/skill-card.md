## Description:

Recommend a hairstyle and hair color based on the user's face shape and skin tone, then preview them with YouCam (Perfect Corp) AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcam-api](https://clawhub.ai/user/youcam-api)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to get hairstyle and hair-color recommendations from a selfie, then optionally preview a restyle or recolor through YouCam AI. The skill is intended for cosmetic try-on guidance, not hair-health diagnostics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send selfies, hair photos, and reference photos to YouCam/Perfect Corp for processing.

Mitigation: Use only photos the user has the right and consent to upload, and make the external processing expectation clear before running generation.

Risk: The skill requires a YouCam API key and can also read credentials from a local credentials.json file.

Mitigation: Prefer the YOUCAM_API_KEY environment variable, keep credentials.json local if used, and do not commit credentials.

Risk: Generated hairstyle or color previews may not match real-world salon outcomes.

Mitigation: Include the required AI-generated-result disclaimer and advise users to consult a professional stylist for coloring decisions.

## Reference(s):

- [Hair Color & Style Advisor Guide](references/guide.md)
- [Perfect Corp AI Face Analyzer API Reference](https://docs.perfectcorp.com/reference/ai_face_analyzer.md)
- [Perfect Corp AI Skin Tone Analysis API Reference](https://docs.perfectcorp.com/reference/ai_skin_tone_analysis.md)
- [Perfect Corp AI Hairstyle API Reference](https://docs.perfectcorp.com/reference/ai_hairstyle.md)
- [Perfect Corp AI Hair Color API Reference](https://docs.perfectcorp.com/reference/ai_hair_color.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and returned image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a YouCam result image URL returned exactly as provided by the API, plus a recommendation rationale and AI-generated-result disclaimer.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
