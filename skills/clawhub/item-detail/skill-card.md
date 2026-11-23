## Description:

根据商品图片和卖点生成带中文排版的电商详情页模块。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营者和商品内容创作者可用商品图片与经核实的卖点，制作带中文文案的详情页视觉模块。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and copy are sent to external AI providers during generation.

Mitigation: Check the chosen provider's data handling before use and send only material you are authorized to share.

Risk: The security scan is incomplete at 55.6% coverage and cannot establish that uninspected components are safe.

Mitigation: Review provider and upload behavior and the undeclared tool scope before use; treat the scan as incomplete.

Risk: The security guidance flags a versioning concern.

Mitigation: Review release and version information before deployment.

## Reference(s):

- [Model flags](artifact/references/model-flags.md)
- [Provider CLI and data flow](artifact/references/provider-cli.md)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/item-detail)

## Skill Output:

**Output Type(s):** [Images, Guidance]

**Output Format:** [Product-detail image files, typically JPG, with Chinese text and layout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images are generated as separate page modules; review text and substantiate product claims before publishing.]

## Skill Version(s):

1.0.35 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
