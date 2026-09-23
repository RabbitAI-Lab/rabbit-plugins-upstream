## Description:

Transforms white-background product photos into realistic lifestyle scene images while preserving the product and matching shadows, reflections, and lighting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators, operators, and developers use this skill to turn clean product images into commercial scene images while keeping the item faithful and physically grounded in the new environment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, reference images, and prompts may be sent to dLazy or another configured image-generation provider.

Mitigation: Use only providers approved for the workflow and avoid confidential product photos unless that provider is authorized.

Risk: Generated files are saved locally to user-selected paths.

Mitigation: Review save paths before execution and keep generated assets in the intended project or output directory.

Risk: Background replacement can create misleading product scenes or alter perceived product qualities.

Mitigation: Review outputs against the source product image and reject scenes that change product shape, color, material, logo, or reasonable use context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-change-background)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands; generated assets are local image files when executed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts, selected images, provider settings, and save paths determine the generated output.]

## Skill Version(s):

1.0.12 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
