## Description:

Turns a static product image into a short 3–5 second listing video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative operators use this skill to turn an existing product image into a short listing video with controlled camera and material motion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The request may be routed to a still-image service despite a video-model selection, sending the image and prompt while returning the wrong media type.

Mitigation: Select a video-capable provider explicitly and use --dry-run to verify the actual model and endpoint; confirm the result is video before starting a batch.

Risk: Submitted images, prompts, and optional brand references are sent to the selected cloud provider.

Mitigation: Use only approved content and confirm the selected provider is appropriate before execution.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Video backend guidance](artifact/references/video-backends.md)
- [Provider and data-flow guidance](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Video files]

**Output Format:** [Short video file, typically MP4]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Usually 3–5 seconds, generated from one product image and a motion prompt; provider and model determine the actual output.]

## Skill Version(s):

1.0.21 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
