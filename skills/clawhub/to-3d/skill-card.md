## Description:

平铺图转隐形模特立体图。平铺图转为有体积感与版型的立体展示图，用于响应“转 3D”“立体图”“隐形模特”“把衣服撑起来”等服装图像生成请求。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce operators, designers, and agents use this skill to turn flat-lay garment photos into ghost-mannequin product images that show volume, drape, collar depth, shadows, and material detail without using a visible model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image inputs and prompts may be sent to the configured external provider.

Mitigation: Use only garment images and prompts that are acceptable to share with that provider, and confirm provider selection before running generation.

Risk: Arguments can reference local paths or URLs outside the intended garment image set.

Mitigation: Avoid arbitrary URLs, keep input paths inside a trusted image folder, and run a dry run before paid generation.

Risk: Untrusted content could influence file or URL arguments used by the helper scripts.

Mitigation: Run the skill in a constrained workspace and review commands before execution when inputs are not fully trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/to-3d)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [Example flat-lay input](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/to-3d/garment-flatlay.jpg)
- [Example 3D product output](https://raw.githubusercontent.com/dlazy-ai/ecommerce-skills/main/docs/to-3d/example-output.jpg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides image generation for apparel product photos and may save JPEG outputs through the configured provider.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
