## Description:

Changes a white-background product photo into a realistic lifestyle scene while preserving the product and matching shadows, reflections, and lighting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, designers, and agents use this skill to turn plain product images into believable commercial scene images. It helps preserve product shape, material, color, and logo while generating or compositing a new background.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, background references, and prompts may be sent to the selected cloud image-generation provider.

Mitigation: Use only approved providers, use dry-run or explicit provider selection when needed, and avoid confidential or unreleased assets unless that provider is approved for them.

Risk: Generated scene images can become misleading if the background implies unsupported product properties or if product details are changed.

Mitigation: Keep product shape, color, material, and logo faithful, require grounded shadows and matching light, and avoid scenes the skill identifies as misleading.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-change-background)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown instructions with inline shell commands and prompt templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local image files when the generated commands are executed with an approved provider.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
