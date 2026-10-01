## Description:

Generates Chinese-language ecommerce product-detail image modules from a product image and supplied selling points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and ecommerce designers use this skill to create product-detail banners, selling-point panels, material descriptions, and specification images with Chinese copy for listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and copy are sent to the selected external generation provider.

Mitigation: Use only assets approved for provider transfer, check active credentials and destination, and preview requests with dry-run.

Risk: Generated Chinese text, product appearance, or claims may be inaccurate.

Mitigation: Proofread every image, compare the product with the source, and verify selling points and specifications before publishing.

## Reference(s):

- [ClawHub item-detail release](https://clawhub.ai/dlazyai/skills/item-detail)
- [Provider CLI and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Product-detail image files with Chinese typography, accompanied by generation prompts and commands]

**Output Parameters:** [2D image modules]

**Other Properties Related to Output:** [Individual modules may be assembled into a longer listing image after visual and copy review.]

## Skill Version(s):

1.0.15 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
