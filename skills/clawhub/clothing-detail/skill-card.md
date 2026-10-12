## Description:

Helps create close-up clothing detail shots from garment photos for e-commerce product pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and content creators use this skill to plan and generate macro views of visible garment details, such as seams, cuffs, and fabric texture, for product listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clothing images and prompts may be sent to a configured cloud image provider.

Mitigation: Only submit images you are comfortable sharing with the selected provider; avoid sensitive local images.

Risk: Image-generation requests may incur charges or produce details not visible in the source garment.

Mitigation: Use dry-run to inspect requests and costs, then verify that the requested detail and generated image match the garment.

Risk: Provider credentials could be exposed if shared unnecessarily.

Mitigation: Provide only the key required for the provider you intend to use.

## Reference(s):

- [Clothing Detail on ClawHub](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [Provider CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with image-generation prompts and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can save generated clothing-detail images locally; review each image against the source garment.]

## Skill Version(s):

1.0.20 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
