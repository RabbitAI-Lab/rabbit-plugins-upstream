## Description:

Helps turn a product's main image into a short ecommerce video with subtle camera movement and material effects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and content creators use this skill to plan and generate short product-listing videos from existing product photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic provider selection may send product photos to an unintended third-party service, including a backend unsuitable for video.

Mitigation: Choose a video-capable provider explicitly and preview the destination with --dry-run before sending sensitive media.

Risk: Generated video may distort the product or fail marketplace video requirements.

Mitigation: Test one short clip, inspect the result, and check the target marketplace's specifications before publishing or generating a batch.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Video backend configuration](references/video-backends.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Running the commands can generate a 3–5 second MP4 video; check marketplace requirements before publishing.]

## Skill Version(s):

1.0.10 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
