## Description:

根据服装图和姿势参考图生成模特上身的电商商品图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商卖家、品牌团队和商品内容创作者可将服装图与姿势或场景参考图合成为模特上身商品图，用于商品目录和 SKU 视觉内容。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input images, including identifiable faces or unreleased product assets, are sent to the selected external provider for processing.

Mitigation: Use only images approved for external processing, and check the selected provider's data handling terms before uploading sensitive assets.

Risk: The security scan was incomplete: only 5 of 9 components were fully inspected and some checks were degraded.

Mitigation: Review the full release artifact and its permissions before installing or using it.

## Reference(s):

- [Provider setup, data flow, and output reference](references/provider-cli.md)
- [Image model command reference](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images]

**Output Format:** [Generated JPEG, PNG, or WebP image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One or more product images; format and batch count depend on the selected options.]

## Skill Version(s):

1.0.34 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
