## Description:

Creates square ecommerce product images with Chinese selling-point copy and promotional badges from a product photo and supplied claims.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and marketing teams use this skill to turn a product photo and verified selling points into a square promotional main image with readable Chinese copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, sales copy, and prompts are sent to the selected image-generation provider.

Mitigation: Use an approved provider for confidential assets and check the data flow before submitting unreleased products.

Risk: Image generation can incur provider charges.

Mitigation: Use dry-run or provider selection to check cost before generating batches.

Risk: Generated text, product details, or promotional claims may be inaccurate.

Mitigation: Review the image at thumbnail size and verify product fidelity and all claims and promotions before publication.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Provider CLI guide](references/provider-cli.md)
- [Model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [Square ecommerce images with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review generated Chinese text, product appearance, and promotional claims before publication.]

## Skill Version(s):

1.0.23 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
