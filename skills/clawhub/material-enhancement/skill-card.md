## Description:

Guides agents in restoring clothing texture in product photography using a high-resolution image of the same garment as a reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and agents use this skill to improve blurry garment texture in product images while aiming to preserve the model, composition, garment shape, and color.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be processed by the configured cloud provider.

Mitigation: Avoid sensitive or private images and use only providers whose data handling is acceptable for the task.

Risk: The bundled generator supports unrelated image-generation tasks and multiple cloud providers.

Mitigation: Select the material-enhancement task explicitly and restrict provider credentials or remove the shared generator if other tasks are unnecessary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Provider CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and commands; generated JPEG or other supported image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an original image and a high-resolution reference image; generated images should be checked for unintended changes.]

## Skill Version(s):

1.0.23 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
