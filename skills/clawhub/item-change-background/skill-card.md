## Description:

Places product photos into realistic scenes with matching lighting, reflections, and contact shadows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and product marketers use this skill to create lifestyle scenes from product photos while aiming to preserve the product's appearance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to a cloud image provider.

Mitigation: Confirm the provider is approved for the assets, use a dry run where possible, and keep API keys scoped and revocable.

Risk: Generated images may change product details or suggest misleading product use.

Mitigation: Review product features and scene realism before publishing; reject altered products or unsupported usage scenes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/item-change-background)
- [Provider CLI reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image-generation commands can save edited product images as JPEG, PNG, or WebP files.]

## Skill Version(s):

1.0.18 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
