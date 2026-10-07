## Description:

Turns a product photo and verified selling points into an ecommerce hero image with Chinese marketing copy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and marketing teams use this skill to create square product hero images with readable Chinese selling points and promotional badges from supplied product photos and approved copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and campaign copy are sent to the selected image provider.

Mitigation: Confirm the chosen provider and credentials before sending sensitive material; inspect the request with dry-run first.

Risk: Generated text or product details may be inaccurate or make unsupported promotional claims.

Mitigation: Verify product appearance, Chinese text, selling points, and promotions against approved source material before publication.

Risk: The sample brand configuration may not match the intended store or market.

Mitigation: Review and edit the example brand settings before reuse.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Image provider and CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Images, Guidance, Shell commands]

**Output Format:** [Product hero image files with Chinese copy; generation and review guidance in Markdown]

**Output Parameters:** [2D image, normally square; optional 3:4 layout]

**Other Properties Related to Output:** [Product appearance, Chinese text legibility, and promotional claims require human review.]

## Skill Version(s):

1.0.17 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
