## Description:

Helps restore garment fabric texture in product photos using a high-resolution image of the same item while aiming to preserve the model, composition, and color.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and product photographers use this skill to improve blurry fabric detail in apparel images using a sharp photo of the same garment, without intentionally changing the model or scene.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source and reference images are sent to the selected cloud image provider.

Mitigation: Use only images approved for transfer and review the selected provider's privacy policy before sending sensitive material.

Risk: Generated images may change details beyond the intended fabric texture.

Mitigation: Compare outputs with the source image and check the model, background, garment color, and silhouette before use.

Risk: Cloud generation can incur charges or save results to an unintended location.

Mitigation: Preview requests with --dry-run and set --save to an intentional, separate output path.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Provider CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Running the commands can save generated images to a chosen local path.]

## Skill Version(s):

1.0.20 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
