## Description:

Turns a product image into a short main-image video with controlled camera motion and subtle material animation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and content creators use this skill to plan and generate 3–5 second product-listing videos from an existing product image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, prompts, and optional brand references may be sent to the configured cloud provider.

Mitigation: Use only a provider approved for the data, and avoid private or sensitive local images.

Risk: An unintended model or unchecked video output may increase cost or misrepresent the product.

Mitigation: Set the intended provider and video model explicitly, dry-run first, then review a single clip and listing requirements before batching.

## Reference(s):

- [Main Image Video on ClawHub](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Video backend configuration](references/video-backends.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can generate a short MP4 from a product image; dry-run previews the request.]

## Skill Version(s):

1.0.16 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
