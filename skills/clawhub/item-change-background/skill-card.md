## Description:

商品换背景。白底商品图 -> 逼真场景图，光影与投影匹配新环境。当用户说「换背景」「加场景」「白底转场景」「放到桌面上」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and ecommerce content teams use this skill to turn plain product photos into photorealistic lifestyle scene images while preserving the product shape, color, material, and logo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected input images may be sent to cloud image-generation providers.

Mitigation: Avoid sensitive images and confirm that the chosen provider credentials and data handling are acceptable before execution.

Risk: The bundled runner exposes generation tasks beyond product background replacement, including watermark removal and video generation.

Mitigation: Confirm the exact task before execution and restrict use to authorized product-background workflows with clear rights to the source content.

Risk: Generated scenes may make a product appear to have properties or usage contexts that the source product does not support.

Mitigation: Review outputs before publication to confirm product identity is preserved and the scene does not imply misleading product capabilities.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/item-change-background)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with CLI command examples and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local image files when the generated commands are executed.]

## Skill Version(s):

1.0.5 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
