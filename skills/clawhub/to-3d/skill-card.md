## Description:

Guides agents in turning flat-lay clothing photos into dimensional ghost-mannequin product images while preserving garment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and product photographers use this skill to guide image generation from single flat-lay garment photos into ghost-mannequin catalog images with visible volume and consistent garment details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to the selected external image provider.

Mitigation: Confirm the provider's data handling before sending unreleased or sensitive product imagery.

Risk: Image generation may incur provider credits or charges.

Mitigation: Preview the request and estimated cost with --dry-run before generating images.

Risk: Generated images may distort a garment's shape, details, or add visible mannequin parts.

Mitigation: Check output against the source image for proportions, pattern, labels, collar, and unwanted body or mannequin elements before publication.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/to-3d)
- [Provider CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell command examples and image-generation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides JPEG product-image generation in square or portrait formats; generated images require visual review for garment fidelity.]

## Skill Version(s):

1.0.18 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
