## Description:

Guides agents in turning a product image into a short main-image video using an explicitly selected video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and developers use this skill to turn existing product images into short listing videos with controlled camera motion and product appearance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled generation tools have broader image-generation and network capabilities than the video-only description suggests.

Mitigation: Review the requested action and run a dry-run before using the tools.

Risk: Automatic provider selection may choose an unintended service when image-only API keys are configured.

Mitigation: Explicitly select the intended provider and video model before generating.

Risk: Product images or referenced URLs may be sent to a generation provider.

Mitigation: Do not pass sensitive product images or internal URLs; review the provider and data flow first.

## Reference(s):

- [ClawHub release: main-image-video](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Video backend configuration](references/video-backends.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may generate short MP4 product videos through an external provider; a dry-run option previews the request.]

## Skill Version(s):

1.0.18 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
