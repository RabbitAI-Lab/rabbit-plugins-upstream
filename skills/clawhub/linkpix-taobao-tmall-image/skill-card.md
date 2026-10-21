## Description:

帮助淘宝和天猫商家通过青虎AI制作商品主图套图、详情页图片和促销活动图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

淘宝和天猫运营人员、设计师及品牌团队用它来制作商品主图、详情页图片和促销海报，并获取生成图片的链接。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading mutable third-party Node/npm tooling can change the local environment.

Mitigation: Review installation first; prefer an already installed, pinned qhkit version and avoid persistent PATH or shell-profile changes unless intended.

Risk: API credentials and uploaded product images are shared with the QinghuAI service.

Mitigation: Use an appropriately scoped token, protect it from logs and chat history, and upload only images approved for the service.

Risk: Image-generation submissions spend account credits.

Mitigation: Check the estimate and submission parameters and obtain explicit user approval before generating images.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-taobao-tmall-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [QinghuAI API key instructions](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with commands and generated image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are returned as links; submissions consume account credits after user confirmation.]

## Skill Version(s):

0.1.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
