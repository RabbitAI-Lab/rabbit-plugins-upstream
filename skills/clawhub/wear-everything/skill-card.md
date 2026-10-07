## Description:

Guides creation of on-model ecommerce images from accessory product photos and model references, with attention to placement, perspective, and shadows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce teams and creators use this skill to place shoes, bags, and accessories onto model reference photos for product imagery while checking placement and product fidelity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product and model images and prompts are sent to the selected cloud image provider.

Mitigation: Use only images approved for sharing, omit unrelated private files, and review available provider credentials before generation.

Risk: Generation may incur provider charges or save output to an unintended location.

Mitigation: Check the selected provider, estimated cost, and output destination with --dry-run before running.

Risk: Generated images may misplace accessories, alter product details, or change a person's appearance.

Mitigation: Inspect placement, product fidelity, and the model's appearance before publishing; do not present fabricated endorsements.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/wear-everything)
- [Provider CLI and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown instructions and locally saved generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional JSON reports output paths and estimated credits; image format and size are configurable.]

## Skill Version(s):

1.0.17 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
