## Description:

根据商品图自动生成详情页图片套图，整合卖点、场景、参数及营销内容，帮助快速制作电商商品详情页素材。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce operators use this skill to guide an agent through generating ordered product-detail image sets from a required product reference image, optional theme choices, and optional selling-point copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update local qhkit tooling.

Mitigation: Review the qhkit install command and package source before allowing installation or upgrade.

Risk: Product images and optional selling-point copy may be uploaded to the qhkit/LinkPix service.

Mitigation: Use only product assets and copy that are approved for the provider service, and avoid submitting sensitive or unreleased material without approval.

Risk: Image generation can spend service credits.

Mitigation: Run estimation first and require explicit user confirmation of the model, reference images, parameters, and estimated credits before submitting generation.

Risk: The skill requires an API key for qhkit service access.

Mitigation: Handle the API key as a secret, prefer supported configuration or environment-variable paths, and avoid exposing it in logs or conversation output.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/autoagc/skills/linkpix-detail-page)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix/qhkit API key console](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with qhkit commands and JSON parameters; generated image URLs are returned by the qhkit service.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit and a qhkit API token; product images and copy may be uploaded to the provider service, and paid credits are spent only after user confirmation.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
