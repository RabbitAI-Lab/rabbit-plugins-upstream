## Description:

Turns a product image into a short, animated main-image video for an online listing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and content creators use a product photo to generate a 3–5 second listing video with subtle camera or material motion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and related metadata are sent to the selected cloud generation provider.

Mitigation: Preview with dry-run, explicitly choose a trusted provider and model, and check its data handling terms before sharing confidential assets.

Risk: Generated motion can distort product details, and a finished video may not meet a marketplace's listing requirements.

Mitigation: Review a short test clip for product fidelity and manually check the target platform's video specifications before publishing or generating a batch.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Video backend configuration](artifact/references/video-backends.md)
- [Provider CLI and data flow](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Video files, Shell commands, Guidance]

**Output Format:** [MP4 video with text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports a dry-run preview; video generation requires an explicitly selected cloud model.]

## Skill Version(s):

1.0.12 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
