## Description:

Creates e-commerce photo variants by replacing a model, background, or both while aiming to preserve the pictured product.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and creators use this skill to make multiple audience- or setting-specific versions of an existing model or mannequin product photo without intentionally changing the product.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, model photos, face or pose references, and prompts are sent to the chosen cloud generation provider.

Mitigation: Choose the provider and credentials deliberately; upload only images you are comfortable sharing with that provider.

Risk: Using identifiable portraits without permission can misrepresent a person or violate their rights.

Mitigation: Use licensed or consented images and obtain permission before supplying personal or third-party portraits; do not fabricate endorsements.

Risk: Generated images may alter product details or introduce visual defects despite preservation instructions.

Mitigation: Inspect garment color, logos, shape, placement, hands, and lighting against the source before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/one-shot)
- [Provider and credential guidance](references/provider-cli.md)
- [Image model parameters](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Edited product photos (typically JPEG) with Markdown instructions and commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate multiple image variants; review garment details, alignment, hands, and lighting before use.]

## Skill Version(s):

1.0.18 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
