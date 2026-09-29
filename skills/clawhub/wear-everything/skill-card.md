## Description:

Guides agents in placing shoes, bags, and accessories from product photos onto model reference photos with natural fit, perspective, and shadows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and marketers use the skill to prepare realistic on-model accessory images from product and model reference photos, with guidance on placement and visual checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, model references, and prompts are sent to the selected cloud image provider.

Mitigation: Confirm the provider before running; avoid sensitive or unlicensed images and obtain permission for model likenesses.

Risk: Generated placements can alter the product, model, or scene and mislead shoppers.

Mitigation: Review fit, scale, product details, and unchanged areas of the reference photo before publishing.

Risk: Image generation and batch runs can incur charges or apply an unsuitable brand profile broadly.

Mitigation: Use --dry-run to inspect the provider and estimated cost, and review optional brand profiles before applying them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/wear-everything)
- [Provider setup and outputs](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Running the commands can produce saved image files; inspect results before publishing.]

## Skill Version(s):

1.0.14 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
