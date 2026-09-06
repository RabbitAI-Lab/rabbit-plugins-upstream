## Description:

从任意图提取干净商品平铺图。真人图 / 街拍图 → 白底平铺商品图。当用户说「提取衣服」「扒图」「转平铺」「抠成商品图」「从买家秀提取」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, designers, and developers use this skill to turn model photos, street-style images, buyer-show photos, or product screenshots into clean white-background flat-lay product images for catalog assets or downstream product-image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected clothing photos and prompts may be uploaded to dLazy or another configured cloud image provider.

Mitigation: Use only photos you have rights to process, avoid sensitive personal images, and verify the configured provider and API keys before execution.

Risk: The skill may infer occluded garment areas or preserve colors, patterns, and product details imperfectly.

Mitigation: Review generated flat-lay outputs against the source image before commercial use, especially inferred areas, colors, patterns, and brand marks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Provider CLI Reference](artifact/references/provider-cli.md)
- [gpt-image-2 Parameter Reference](artifact/references/model-flags.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash commands, prompt templates, and saved image file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image assets are typically saved as JPEG or PNG flat-lay product images; batch generation may produce multiple candidate files.]

## Skill Version(s):

1.0.5 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
