## Description:

Generates Chinese-language ecommerce product-detail image modules from product photos and selling points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and ecommerce content creators use product photos and supplied selling points to produce Chinese-language banners, feature blocks, material details, and size-reference images for product-detail pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts are sent to the selected image provider.

Mitigation: Use only images approved for that provider; avoid sensitive or unreleased products unless provider terms allow them.

Risk: Image generation can incur provider charges.

Mitigation: Check provider availability and estimate costs with doctor or dry-run mode before generating.

Risk: Generated Chinese text or product claims may be inaccurate.

Mitigation: Proofread text and verify claims against product information before publishing.

## Reference(s):

- [ClawHub item-detail skill](https://clawhub.ai/dlazyai/skills/item-detail)
- [Provider setup and output reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Images, Text, Shell commands]

**Output Format:** [Product-detail image files with Chinese text; Markdown prompts and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Modules can be assembled into a longer detail page; review Chinese text and product claims before publication.]

## Skill Version(s):

1.0.23 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
