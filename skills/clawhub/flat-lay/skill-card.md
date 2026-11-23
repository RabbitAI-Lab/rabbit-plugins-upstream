## Description:

服装平铺图一键上身试穿。服装平铺图 + 姿势参考图 → 模特上身商拍图，款式、颜色、织法、版型保持不变。当用户说「平铺图转模特图」「衣服上身」「虚拟试穿」「AI 试衣」「让模特穿上」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

服装电商团队与内容创作者可将平铺服装图和姿势或场景参考图合成为模特上身商品图，也可组合上装与下装生成整套造型。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment, reference, or face images may be sent to an external provider, and the security scan was partial.

Mitigation: Before use, check which provider will receive the images and confirm that the images are appropriate to share; treat the partial scan as incomplete assurance.

## Reference(s):

- [Provider and data flow guidance](references/provider-cli.md)
- [Image model parameters](references/model-flags.md)
- [dLazy CLI repository (referenced by the skill)](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images]

**Output Format:** [JPEG or another supported image file, saved to the requested path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image dimensions, quality, format, and batch count depend on the selected options; the documented default is 1024×1536 JPEG.]

## Skill Version(s):

1.0.35 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
