## Description:

Virtual clothes try-on studio using YouCam (Perfect Corp) AI to swap outfits onto a user's photo, optionally change the background, and optionally turn the result into a short motion video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcam-api](https://clawhub.ai/user/youcam-api)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill through an agent to preview outfit, background, and short motion-video variations from person photos and garment references. Agent operators use it to route virtual try-on requests through YouCam/Perfect Corp APIs while disclosing credit costs and generated-media limitations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Person photos, garment images, generated prompts, and produced media are sent to YouCam/Perfect Corp services, and video prompt enhancement may involve Gemini.

Mitigation: Install only when this data sharing is acceptable for the user and use case; avoid submitting sensitive images or prompts without appropriate consent.

Risk: API credentials may be stored in a local credentials file.

Mitigation: Prefer the YOUCAM_API_KEY environment variable and restrict access to any local credentials file.

Risk: The skill installs Python dependencies before calling external APIs.

Mitigation: Review and pin dependencies before use in controlled or production environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youcam-api/skills/youcam-clothes-tryon-studio)
- [Clothes Try-on Studio Guide](references/guide.md)
- [Perfect Corp AI Clothes Reference](https://docs.perfectcorp.com/reference/ai_clothes.md)
- [Perfect Corp AI Photo Background Change Reference](https://docs.perfectcorp.com/reference/ai_photo_background_change.md)
- [Perfect Corp AI Video Generator Reference](https://docs.perfectcorp.com/reference/ai_video_generator.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown text with command snippets and returned media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns result image or video URLs exactly as provided and includes an AI-generated reference-media notice.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
