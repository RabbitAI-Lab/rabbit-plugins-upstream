## Description:

Generates Chinese-language e-commerce product-detail image modules from product photos and selling-point copy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and designers use this skill to turn product photos and verified selling points into Chinese-text banners, feature blocks, material details, and specification modules for product listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, prompts, and selling-point copy are sent to the selected cloud image provider.

Mitigation: Inspect requests with --dry-run, choose an approved provider, and avoid confidential images or internal paths unless approved for that provider.

Risk: Generated Chinese text, product details, or marketing claims may be inaccurate.

Mitigation: Proofread every image, compare product details with the source, and verify all claims before publishing.

## Reference(s):

- [ClawHub item-detail release](https://clawhub.ai/dlazyai/skills/item-detail)
- [Provider CLI and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Images, Text guidance, Shell commands]

**Output Format:** [Image files with Markdown guidance and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separate visual modules are assembled into a product-detail page after review.]

## Skill Version(s):

1.0.24 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
