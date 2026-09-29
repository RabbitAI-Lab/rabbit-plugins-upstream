## Description:

Turns flat-lay clothing photos into dimensional ghost-mannequin product images while aiming to preserve garment details and proportions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and product-image creators use this skill to turn flat-lay garment photos into ghost-mannequin images for product listings without photographing a model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to dLazy or a selected cloud model provider.

Mitigation: Avoid confidential images unless the provider's access and retention terms are acceptable.

Risk: Image generation can incur provider charges.

Mitigation: Use dry-run to review the selected provider and estimated cost before generation.

Risk: Provider credentials may be exposed if shared or included in outputs.

Mitigation: Keep API keys private and out of shared prompts and files.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/to-3d)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Image model flags](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown instructions and generated JPEG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Square or portrait images; optional batches and local file saving.]

## Skill Version(s):

1.0.14 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
