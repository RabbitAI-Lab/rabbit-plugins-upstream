## Description:

Recommends makeup looks from a user's selfie, using YouCam/Perfect Corp analysis to assess face shape and skin tone and generate a virtual makeup try-on preview.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcam-api](https://clawhub.ai/user/youcam-api)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to get makeup recommendations and virtual try-on previews from a clear front-facing selfie. The agent analyzes makeup-relevant facial attributes, explains why a look suits the user, and returns the generated try-on image URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads selfies to YouCam/Perfect Corp for facial analysis and virtual makeup generation.

Mitigation: Review before installing if this data flow is not acceptable, use only selfie images intended for processing, and avoid public image URLs when possible.

Risk: The skill requires a YouCam API key and may read credentials from a local credentials.json file.

Mitigation: Prefer the YOUCAM_API_KEY environment variable and do not commit real credentials to the skill directory.

Risk: The facial-analysis API can request attributes broader than makeup recommendations require.

Mitigation: Limit requests to makeup-relevant attributes such as faceShape and color information, and avoid age or gender attributes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youcam-api/skills/youcam-beauty-advisor)
- [Perfect Corp AI Face Analyzer documentation](https://docs.perfectcorp.com/reference/ai_face_analyzer.md)
- [Perfect Corp AI Skin Tone Analysis documentation](https://docs.perfectcorp.com/reference/ai_skin_tone_analysis.md)
- [Perfect Corp Makeup VTO documentation](https://docs.perfectcorp.com/reference/makeup_vto.md)
- [Perfect Corp AI Look VTO documentation](https://docs.perfectcorp.com/reference/ai_look_vto.md)
- [Beauty Advisor recommendation guide](references/guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with recommendation rationale, setup or execution commands when needed, the exact result image URL, and a required disclaimer.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill states YouCam credit costs before generation and runs only the preview option the user chooses.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
