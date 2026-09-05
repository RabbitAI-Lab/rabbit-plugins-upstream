## Description:

Analyze portrait photos to recommend flattering hairstyles based on face shape, facial features, hair texture, and personal style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nellyxiaolong-cmyk](https://clawhub.ai/user/nellyxiaolong-cmyk)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to get personalized hairstyle recommendations from a portrait or headshot. The skill helps produce face and hair analysis, recommended styles, barber or stylist communication notes, alternatives, and optional image-generation prompts or previews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on uploaded portrait photos for face and hair analysis.

Mitigation: Use only photos the user has consented to share, and avoid analyzing third-party photos without permission.

Risk: Optional AI hairstyle previews may process portrait data through an image-generation provider.

Mitigation: Confirm the active image-generation provider and privacy posture before requesting preview generation.

Risk: Photo quality, hair texture, and stylist execution can affect whether a recommendation works in practice.

Mitigation: Present generated previews and haircut guidance as references, and clearly note uncertainty when image evidence is insufficient.

## Reference(s):

- [Hairstyle Knowledge Reference](references/hairstyles.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report with hairstyle recommendations, haircut instructions, alternatives, and optional image-generation prompt text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference user-provided portrait photos and may request image generation for visual previews.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
