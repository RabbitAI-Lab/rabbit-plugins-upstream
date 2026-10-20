## Description:

Transforms an existing product-on-model photo into versions with a different model, background, or both while aiming to preserve the product.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and creators use an existing model or mannequin photo to make product imagery for different audiences or settings while retaining the garment's appearance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product or model photos and prompts are sent to the chosen image provider.

Mitigation: Use only photos permitted by the provider's terms; avoid private or regulated images and keep API keys scoped and revocable.

Risk: Image generation can incur charges and alter garment details or anatomy.

Mitigation: Review request and estimated cost with dry-run, then inspect generated images for garment fidelity, hands, and lighting before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/one-shot)
- [Provider setup and output guide](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Image files, Text guidance, Shell commands]

**Output Format:** [Generated JPEG, PNG, or WebP images with optional JSON status and file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports multiple image variants and a dry run for cost review.]

## Skill Version(s):

1.0.23 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
