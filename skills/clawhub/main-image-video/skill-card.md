## Description:

Turns one static ecommerce main product image into a short 3-5 second main-image product video with controlled camera motion and material movement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketers, and agents use this skill to create short product-slot videos from existing product imagery before publishing or batch generation. It is intended for simple main-image video clips, not long-form ads, talking-head videos, or product redesign.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be uploaded to the selected cloud generation backend.

Mitigation: Use only backends acceptable for the product data, avoid confidential images unless approved, and set --provider explicitly.

Risk: Video generation can consume paid credits or API spend.

Mitigation: Run with --dry-run first and generate a single short clip before scaling to batch work.

Risk: An unspecified or unsuitable video model can cause failed requests or unexpected output.

Mitigation: Set DLAZY_VIDEO_MODEL or pass --model explicitly for the selected backend before execution.

Risk: Model output may distort the product or amplify flaws from the source image.

Mitigation: Inspect and repair the still image first, use subtle motion prompts, and manually review the video against platform requirements before publishing.

Risk: The example brand profile contains demographic defaults that may not fit the user's brand or audience.

Mitigation: Customize brand.yaml before using it for production prompts or batch generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Video backend configuration](references/video-backends.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides generation of MP4 video files through configured cloud video backends; dry-run mode can preview requests before API spend.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
