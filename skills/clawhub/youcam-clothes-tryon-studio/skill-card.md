## Description:

Virtual clothes try-on studio using YouCam (Perfect Corp) AI. Swap outfits onto the user's photo, optionally change the background, and optionally turn the result into a short motion video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcam-api](https://clawhub.ai/user/youcam-api)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to run a guided virtual clothing try-on flow, optionally replacing the background and generating a short motion video from the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal photos, garment images, and optional video prompts are sent to YouCam/Perfect Corp, with video prompts potentially processed through Gemini as described by the API schema.

Mitigation: Install and use only when that external processing is acceptable, prefer local image uploads over public image URLs, and avoid submitting sensitive images or prompts.

Risk: Generation steps consume YouCam credits, and video is billed per second.

Mitigation: Check feature costs and credit balance before running generation, state the total expected cost, and run only the steps the user confirms.

Risk: Generated try-on imagery may not reflect actual garment fit or appearance.

Mitigation: Present outputs as AI-generated reference material and include the required note that actual fit and appearance may vary.

## Reference(s):

- [Clothes Try-On Studio Guide](references/guide.md)
- [Perfect Corp AI Clothes API](https://docs.perfectcorp.com/reference/ai_clothes.md)
- [Perfect Corp AI Photo Background Change API](https://docs.perfectcorp.com/reference/ai_photo_background_change.md)
- [Perfect Corp AI Video Generator API](https://docs.perfectcorp.com/reference/ai_video_generator.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns result image or video URLs exactly as provided by the API and includes an AI-generated reference-only note.]

## Skill Version(s):

1.0.1 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
