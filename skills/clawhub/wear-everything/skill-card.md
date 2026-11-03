## Description:

鞋包配饰真人穿戴图。商品图 + 模特参考图 → 真人佩戴图，落位、透视与阴影自然。当用户说「鞋包上脚」「配饰上身」「墨镜戴上」「首饰佩戴图」「包包上身」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce creators use the skill to turn product and model reference images into on-model photos of shoes and accessories. It guides product placement and image-generation prompts while aiming to preserve the rest of the reference scene.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portraits and commercial image assets may be sent to the selected cloud provider; service retention was not verified.

Mitigation: Use only images you are authorized to share and review the selected provider's privacy terms before uploading.

Risk: Image generation can incur credits, and saving may overwrite an existing file.

Mitigation: Choose the provider explicitly and use --dry-run to review the images, destination, and estimated cost; save only where overwriting is acceptable.

## Reference(s):

- [Model flags](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Files, Shell commands, Guidance]

**Output Format:** [Generated image files (commonly JPEG) with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation uses product images and a model or scene reference; output location and image options are configurable.]

## Skill Version(s):

1.0.29 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
