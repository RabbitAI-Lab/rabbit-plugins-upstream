## Description:

Generates Chinese-language e-commerce product detail image modules from product photos and selling points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and designers use this skill to create Chinese-language product detail banners and modules from product images and verified selling points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and referenced image URLs are sent to the selected generation provider.

Mitigation: Use only assets and URLs approved for sharing with that provider; avoid private intranet or signed URLs and regulated customer data unless the provider agreement permits them.

Risk: Generated Chinese text or product claims may be inaccurate or misleading.

Mitigation: Review rendered characters and verify all product attributes, certifications, and promotional claims before publication.

## Reference(s):

- [Item Detail skill release](https://clawhub.ai/dlazyai/skills/item-detail)
- [Provider CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [JPEG or PNG product-detail images with Markdown instructions and optional JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates separate banner, selling-point, material, detail, or specification modules; review Chinese lettering and product claims before publishing.]

## Skill Version(s):

1.0.18 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
