## Description:

Generates Chinese-language e-commerce product-detail image modules from product photos and supplied selling points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and designers use a product photo and verified selling points to create Chinese-language product-detail banners, feature panels, material and detail panels, and specification blocks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and optional brand constraints are sent to the configured cloud image provider.

Mitigation: Use approved images and brand materials only; avoid sensitive or confidential inputs unless cloud processing is authorized.

Risk: Generating multiple image modules or batches can consume provider credits.

Mitigation: Use dry-run to inspect the request and estimated cost before generating images.

Risk: Generated Chinese text or product details may be inaccurate.

Mitigation: Proofread every image, confirm product appearance, and substantiate claims before publication.

Risk: The optional npx installation command runs externally supplied package code.

Mitigation: Review the package and command before running an optional npx install.

## Reference(s):

- [ClawHub item-detail release](https://clawhub.ai/dlazyai/skills/item-detail)
- [Provider setup and output reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Images, Text, Shell commands]

**Output Format:** [Chinese-language image modules saved as JPG files, with Markdown guidance and generation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Modules can be generated separately at different aspect ratios; review text and product fidelity before publishing.]

## Skill Version(s):

1.0.16 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
