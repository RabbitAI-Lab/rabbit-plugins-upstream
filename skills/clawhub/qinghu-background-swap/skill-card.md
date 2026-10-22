## Description:

帮助电商用户将商品图片的背景替换为指定场景，生成不同风格的营销图片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营和设计人员可提供商品图片与目标场景描述，生成不同背景的营销场景图。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the qhkit command-line package changes the local Node environment and may leave configuration behind.

Mitigation: Install only if you trust the package and service; review and remove local tooling or configuration when no longer needed.

Risk: An API token and selected product images are used with the provider service.

Mitigation: Keep the token private and upload only images approved for the provider.

Risk: Generation may consume account credits and alter text, logos, or product details.

Mitigation: Check the credit estimate before generating and inspect the returned images before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-background-swap)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [青虎AI API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Images, Text guidance]

**Output Format:** [Image URLs with a short completion message and credits consumed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images may alter product details; review text, logos, and product structure.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
