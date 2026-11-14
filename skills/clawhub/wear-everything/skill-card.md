## Description:

鞋包配饰真人穿戴图。商品图 + 模特参考图 → 真人佩戴图，落位、透视与阴影自然。当用户说「鞋包上脚」「配饰上身」「墨镜戴上」「首饰佩戴图」「包包上身」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users creating ecommerce product imagery can combine a product photo with a model or scene reference to generate an on-model image of shoes, bags, and other accessories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product and model images, along with prompts, may be sent to an external image provider for generation.

Mitigation: Review which images and prompt content will be uploaded, confirm the provider, and authorize the transfer; avoid sensitive images.

Risk: The security evidence reports partial analysis and flags tool scope and an unpinned `npx skills` reference for review.

Mitigation: Review the skill and its tool scope before installation, including the package or source invoked through `npx skills`.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [Model Flags Reference](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [Wear Everything on ClawHub](https://clawhub.ai/dlazyai/skills/wear-everything)

## Skill Output:

**Output Type(s):** [Image files, Guidance, Shell commands]

**Output Format:** [Generated JPEG images by default, with Markdown prompt templates and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images can be saved to a requested path; JPEG, PNG, or WebP output is supported.]

## Skill Version(s):

1.0.32 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
