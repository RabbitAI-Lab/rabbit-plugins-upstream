## Description:

Recommend and preview makeup looks based on the user's face shape and skin tone, using YouCam (Perfect Corp) AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcam-api](https://clawhub.ai/user/youcam-api)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to recommend makeup looks from a clear, front-facing selfie and preview the selected look with YouCam virtual try-on. It is intended for makeup recommendations and previews, not skin-condition scoring, hair, clothes, or unrelated attribute inference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends selected selfies or image URLs to Perfect Corp/YouCam for face analysis and makeup rendering.

Mitigation: Install and use the skill only when this external processing is acceptable, and provide only images the user is comfortable sharing for the makeup preview.

Risk: API credentials may be exposed if stored directly in local files.

Mitigation: Prefer YOUCAM_API_KEY through an environment or platform secret, and use credentials.json only when local file-based secrets are appropriate.

Risk: Face analysis features can expose unrelated attributes such as age or gender if requested outside the makeup workflow.

Mitigation: Limit use to face-shape, ratio, and color signals needed for makeup recommendations, and avoid asking the skill to infer unrelated attributes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youcam-api/skills/youcam-beauty-advisor)
- [Beauty Advisor Recommendation Guide](references/guide.md)
- [Perfect Corp AI Face Analyzer API](https://docs.perfectcorp.com/reference/ai_face_analyzer.md)
- [Perfect Corp AI Skin Tone Analysis API](https://docs.perfectcorp.com/reference/ai_skin_tone_analysis.md)
- [Perfect Corp Makeup VTO API](https://docs.perfectcorp.com/reference/makeup_vto.md)
- [Perfect Corp AI Look VTO API](https://docs.perfectcorp.com/reference/ai_look_vto.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with a recommendation rationale, the returned result image URL, and a fixed AI-generated preview note]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The result image URL should be returned exactly as provided by the YouCam API.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
