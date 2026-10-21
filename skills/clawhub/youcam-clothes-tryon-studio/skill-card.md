## Description:

Uses YouCam to try garments on a person's photo, with optional background replacement and short motion video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcam-api](https://clawhub.ai/user/youcam-api)

### License/Terms of Use:

MIT-0

## Use Case:

People creating outfit previews can try a garment on a supplied photo, optionally replace the background, and generate a short motion video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected person and garment photos, and optional prompt text, are sent to Perfect Corp/YouCam for processing.

Mitigation: Share only photos and prompts you are comfortable sending to the provider; review its privacy and retention terms before using sensitive images.

Risk: Generation steps consume API credits, and retrying a still-running job can start a second paid task.

Mitigation: Confirm selected steps and their costs before generation; check the existing task status rather than rerunning it.

Risk: AI-generated try-on results may not match actual garment fit or appearance.

Mitigation: Label outputs as AI-generated previews for reference only.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youcam-api/skills/youcam-clothes-tryon-studio)
- [YouCam clothes API](https://docs.perfectcorp.com/reference/ai_clothes.md)
- [YouCam background change API](https://docs.perfectcorp.com/reference/ai_photo_background_change.md)
- [YouCam video generator API](https://docs.perfectcorp.com/reference/ai_video_generator.md)
- [Clothes try-on flow and output guide](references/guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown with image or video result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the steps performed and an AI-generated result disclaimer; generated image or video is accessible at the returned URL.]

## Skill Version(s):

1.1.1 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
