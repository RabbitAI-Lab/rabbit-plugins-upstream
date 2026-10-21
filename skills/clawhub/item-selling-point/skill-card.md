## Description:

Creates Chinese-language ecommerce main images with product selling points and promotional copy from a product photo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and designers use a product photo and verified selling points to create Chinese-language promotional main images for product listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to the selected cloud provider.

Mitigation: Use only images and prompts approved for the selected provider; confirm the provider before running.

Risk: API credentials and generated files can be exposed through careless configuration or output-path choices.

Mitigation: Use scoped, revocable keys and choose local output paths deliberately.

Risk: Generated product text or imagery may contain inaccurate claims, promotions, or distorted details.

Mitigation: Review the image, product fidelity, selling points, and promotion terms before publication.

Risk: External CLI or installation commands may change or be untrusted.

Mitigation: Verify or pin external CLI and installation commands before running them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Provider CLI and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Locally saved image files and text; optional JSON execution results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically generates square product images with Chinese captions and promotional badges.]

## Skill Version(s):

1.0.24 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
