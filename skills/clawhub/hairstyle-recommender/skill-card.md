## Description:

Analyzes portrait photos to recommend flattering hairstyles based on face shape, facial features, hair texture, and personal style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nellyxiaolong-cmyk](https://clawhub.ai/user/nellyxiaolong-cmyk)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill after uploading a portrait or headshot to receive personalized hairstyle recommendations, haircut communication guidance, and optional image-generation prompts or outputs showing the proposed style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portrait analysis and the mandatory image-generation flow can involve sensitive personal images and external image-generation services without clear consent or privacy disclosure.

Mitigation: Tell users before any portrait upload or third-party generation step and offer a clear advice-only path without generating or sending an image.

## Reference(s):

- [Hairstyle knowledge reference](references/hairstyles.md)
- [ClawHub skill page](https://clawhub.ai/nellyxiaolong-cmyk/skills/hairstyle-recommender)
- [Publisher profile](https://clawhub.ai/user/nellyxiaolong-cmyk)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese Markdown with structured portrait analysis, hairstyle recommendations, haircut instructions, and image-generation prompts when direct image generation is unavailable.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated images when an image-generation tool is available; otherwise returns copy-ready prompts.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
