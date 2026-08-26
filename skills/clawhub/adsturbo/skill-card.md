## Description:

AdsTurbo full toolkit for AI spokesperson video, video generation and extension, ad cloning, watermark removal, 4K upscaling, video translation, character swap, motion control, subtitles, AI image generation, and e-commerce photos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to chain AdsTurbo media workflows across digital-human narration, image generation, video generation, ad cloning, enhancement, translation, and transformation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill supports public uploads and media processing that may expose confidential files, private portraits, or voice samples to third-party processing.

Mitigation: Use only public or approved assets, avoid confidential media, and confirm that users accept third-party processing before upload.

Risk: Ad cloning, watermark removal, character swap, voice, and likeness workflows can be misused without rights or consent.

Mitigation: Require confirmation that the user owns or is authorized to modify the source media and has permission to use any depicted likeness or voice.

Risk: Unpinned dependencies can change behavior or introduce vulnerable package versions.

Mitigation: Pin or constrain Python dependencies and review the dependency set before deployment.

## Reference(s):

- [AdsTurbo Skill Page](https://clawhub.ai/adsturbo/skills/adsturbo)
- [AdsTurbo Website](https://www.adsturbo.ai)
- [Digital Human](references/digital_human.md)
- [AI Video Generation](references/video_generation.md)
- [Ad Clone](references/ad_clone.md)
- [Video Enhance](references/video_enhance.md)
- [Video Transform](references/video_transform.md)
- [AI Image Creation](references/image.md)
- [Upload](references/upload.md)
- [Work Status](references/work.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration notes, and generated media result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public asset URLs and ADSTURBO_API_KEY-backed API calls; most media jobs are asynchronous and return workspace IDs or result URLs.]

## Skill Version(s):

1.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
