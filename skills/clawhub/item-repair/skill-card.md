## Description:

Guides agents in retouching product photos for listings by reducing incidental wrinkles, aligning presentation, evening lighting, and cleaning backgrounds while preserving product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and content teams use this skill to prepare cleaner product listing photos while retaining the item's visible design and condition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled generator supports unrelated tasks, including watermark removal, beyond item-photo repair.

Mitigation: Review the package before installing and restrict agent use to the intended item-repair commands and trusted inputs.

Risk: Product images and prompts are sent to a selected cloud provider.

Mitigation: Choose an approved provider and obtain permission before sending confidential or customer-supplied images.

Risk: Retouching may alter design details or conceal product defects.

Mitigation: Compare edited images with originals and reject changes to product construction, colors, or visible damage before publication.

## Reference(s):

- [ClawHub item-repair release](https://clawhub.ai/dlazyai/skills/item-repair)
- [Provider CLI reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can save edited product images locally; inputs and prompts are sent to the selected cloud provider.]

## Skill Version(s):

1.0.24 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
