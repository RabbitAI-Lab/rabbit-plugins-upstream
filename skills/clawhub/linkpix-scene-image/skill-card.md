## Description:

根据商品参考图和场景描述生成单张或成组的电商商品场景图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营人员、设计师和营销团队使用商品图片生成生活方式场景图，用于商品详情页及广告素材。

### Deployment Geography for Use:

China (domestic iqinghu.com service)

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to the LinkPix/iqinghu service.

Mitigation: Review the images and prompts for sensitive information before submitting them.

Risk: Installing or updating the qhkit npm package introduces a third-party dependency.

Mitigation: Use a reviewed or pinned package version in controlled environments.

Risk: An international AutoAGC account or token may not work with this domestic iqinghu.com workflow.

Mitigation: Check which account and service site the token belongs to before configuring it.

Risk: Generative editing may alter product details, including text, logos, and structure.

Mitigation: Review the finished images against the original product before publication.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-scene-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iqinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Image links]

**Output Format:** [Markdown with generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports estimated and actual credit usage; generated images are delivered by URL.]

## Skill Version(s):

0.1.6 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
