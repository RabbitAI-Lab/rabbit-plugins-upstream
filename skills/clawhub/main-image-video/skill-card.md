## Description:

Turns a product image into a short main-image video with controlled camera and material motion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and content teams use this skill to turn existing product images into short product-listing videos without a new shoot.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to the selected generation provider.

Mitigation: Confirm the provider's data handling is acceptable before submitting product assets.

Risk: Video generation may incur provider charges.

Mitigation: Select the intended provider and model explicitly, use dry-run first, and test one short clip before batching.

Risk: Generated motion may distort product details or fail a marketplace's video requirements.

Mitigation: Inspect the source image and generated clip, then check the destination platform's current video specifications before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Video backend configuration](references/video-backends.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance and commands; generated video is saved as an MP4 file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically produces a 3–5 second clip from one product image; requires an explicitly selected video model.]

## Skill Version(s):

1.0.15 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
