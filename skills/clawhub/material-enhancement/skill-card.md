## Description:

Enhances blurred clothing material texture using a high-resolution product image as reference while preserving the original composition, model, background, color, and garment shape.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, creative teams, and agents use this skill to post-process apparel images whose fabric detail is blurred, using a matching high-resolution product image to reconstruct credible texture without changing the subject or scene.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to configured cloud providers during generation.

Mitigation: Use only images and prompts that are approved for the selected provider, and confirm provider credentials and data-handling expectations before running generation commands.

Risk: The bundled generator supports broader ecommerce generation tasks beyond material enhancement.

Mitigation: Use the documented material-enhancement task with the intended two-image input order and review scripts before allowing broader task execution.

Risk: Using a non-matching high-resolution product image can transfer the wrong material texture.

Mitigation: Confirm both input images are the same product before generation and compare the output against the original for color, silhouette, model, and background drift.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Backend call reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline bash commands, prompt templates, and parameter guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documented workflow can save generated image files through the configured image provider.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
