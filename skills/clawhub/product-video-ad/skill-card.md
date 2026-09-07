## Description:

Creates product short-video ads by turning selling points into storyboard scripts, generating each shot, stitching clips, and adding captions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce marketers and agents use this skill to plan and generate 15-30 second product ad videos for paid traffic from product selling points, reference images, storyboard captions, and brand guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Storyboard inputs can trigger broad local file reads, URL fetches, cloud uploads, and writes outside the requested output folder.

Mitigation: Install only when the storyboard files and image paths are trusted, review every dry-run before execution, avoid untrusted board.json files, and keep outputs in a disposable directory.

Risk: Reference images and prompts may be sent to the selected cloud generation backend.

Mitigation: Use only explicitly selected product images and confirm the provider selection before running generation.

Risk: Independently generated shots may vary in product appearance or timing.

Mitigation: Use the same product reference image across shots, apply brand guidance, and review generated clips before publishing the final ad.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Provider CLI Reference](references/provider-cli.md)
- [Video Backend Configuration](references/video-backends.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [Main Image Video Skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/main-image-video/skill.md)
- [UGC Testimonial Skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/ugc-testimonial/skill.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with JSON storyboard inputs and shell commands; generated artifacts include MP4 clips, SRT captions, concat lists, and final MP4 files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Storyboard mode accepts shot IDs, durations, image paths or URLs, prompts, captions, optional brand YAML, and optional subtitles.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
