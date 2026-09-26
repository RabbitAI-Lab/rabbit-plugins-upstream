## Description:

Generates conversion-oriented e-commerce main product images by combining a product image with Chinese selling-point copy and layout guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and developers use this skill to turn a product image and short selling points into a single e-commerce main image with readable Chinese promotional copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and optional brand assets may be sent to the selected generation provider.

Mitigation: Use --dry-run to inspect the request, avoid confidential imagery unless the provider is acceptable, and use trusted CLI installation paths.

Risk: Generated marketing copy or badges could imply unsupported product claims or false promotions.

Mitigation: Verify product functions and promotions before generation, and avoid absolute claims or unverified discounts.

Risk: Generated images may alter product appearance or make Chinese text unreadable at marketplace thumbnail sizes.

Mitigation: Use the skill's product-fidelity prompt constraints, generate multiple candidates, and inspect the final image at thumbnail size before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0-pro parameter reference](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with bash commands and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically saves 1:1 or 3:4 e-commerce image files; batch mode may create multiple candidate outputs.]

## Skill Version(s):

1.0.13 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
