## Description:

Generates Chinese-language ecommerce product-detail image modules from a product photo and supplied selling points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and designers use this skill to turn product photos and approved selling points into Chinese-language banners, feature graphics, and other product-detail modules for review before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, selling-point copy, and prompts are sent to the selected image-generation provider.

Mitigation: Confirm the provider with --dry-run or --doctor and use only assets approved for that provider.

Risk: Generated image files are written to local paths.

Mitigation: Choose and review output paths before generation.

Risk: Generated Chinese text or product claims may be inaccurate.

Mitigation: Proofread every module and verify product details and claims before publication.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/item-detail)
- [Model flags](references/model-flags.md)
- [Provider CLI guide](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [Product-detail image modules with Chinese text, supported by CLI commands and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated modules are saved locally; review Chinese text, product fidelity, and claims before publishing.]

## Skill Version(s):

1.0.19 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
