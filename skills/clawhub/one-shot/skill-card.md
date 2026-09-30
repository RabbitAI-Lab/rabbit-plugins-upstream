## Description:

Guides the creation of e-commerce photos with a different model, background, or both from an existing model or mannequin image while aiming to preserve the product.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce marketers and catalog teams use this skill to create model and setting variants of a photographed garment for different audiences and campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product or model photos and prompts are sent to the configured image-generation provider.

Mitigation: Use --dry-run to check the provider and request; send only intended images and choose an account with acceptable data handling.

Risk: Generated images may change garment details, produce visual defects, or suggest an unauthorized endorsement.

Mitigation: Review garment fidelity, anatomy, and lighting before use; avoid impersonating a real person or implying their endorsement.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/one-shot)
- [Image provider and CLI guidance](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with image-editing prompts and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Running the commands with a configured provider can save generated JPEG catalog images; review results before publishing.]

## Skill Version(s):

1.0.14 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
