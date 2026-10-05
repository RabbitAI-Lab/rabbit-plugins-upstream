## Description:

Generates Chinese-language e-commerce product-detail image modules from product photos and selling points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and designers use this skill to create Chinese-language product-detail banners, feature blocks, material and detail views, and specification graphics from supplied product images and selling points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to the selected image-generation provider.

Mitigation: Confirm the configured provider and avoid sending sensitive or private images.

Risk: Generated assets can be written to a user-selected local path.

Mitigation: Check the save destination before generating files.

Risk: Generated Chinese text, product details, or selling points may be incorrect or misleading.

Mitigation: Proofread image text and verify product claims and visual fidelity before publishing.

## Reference(s):

- [ClawHub item-detail release](https://clawhub.ai/dlazyai/skills/item-detail)
- [Model flags](artifact/references/model-flags.md)
- [Provider and CLI guide](artifact/references/provider-cli.md)
- [dLazy CLI documentation and source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [Chinese-text product-detail image modules and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Modules can be generated separately for banners, selling points, material details, and specifications; review text and claims before publishing.]

## Skill Version(s):

1.0.17 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
