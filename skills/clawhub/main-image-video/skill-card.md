## Description:

Turns a product image into a short main-listing video with controlled camera movement and subtle material motion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and content creators use this skill to turn an existing product image into a short product-listing video without a new shoot.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and optional brand-reference images may be sent to the configured cloud provider.

Mitigation: Choose a trusted provider; avoid confidential local files and internal-only image URLs, and inspect the request with dry-run before sending it.

Risk: Video generation can incur provider charges and produce footage that distorts the product or misses listing specifications.

Mitigation: Set the video model explicitly, test one short clip before batching, and review product fidelity and platform specifications before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Video backend configuration](references/video-backends.md)
- [Provider setup and data flow](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and video prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Execution can save a short MP4 video; duration and quality depend on the selected provider and model.]

## Skill Version(s):

1.0.14 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
