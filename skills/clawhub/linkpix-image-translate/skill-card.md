## Description:

批量翻译商品图片中的文字内容，自动保持原有版式与设计风格，帮助跨境卖家完成多语言商品图本地化。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and agents use this skill to translate ecommerce product images into target languages while preserving the original layout and design style. It supports batch image localization workflows that require cost estimation, explicit confirmation, and review of generated outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may expose API keys if they paste secrets into chat.

Mitigation: Configure credentials through qhkit config, a local secret mechanism, or QHKIT_TOKEN outside the chat, and do not ask users to paste API keys into conversation.

Risk: Selected product images are sent to the Qinghu/LinkPix service and generation consumes credits after confirmation.

Mitigation: Confirm the image set, target language, and estimate output before generation, then proceed only after explicit user approval.

Risk: Generated image translations can contain spelling, pricing, branding, logo, or product-detail errors.

Mitigation: Require visual review of every output image, especially prices, specifications, brand names, logos, and dense text.

Risk: The skill may install or update qhkit or Node tooling and store local configuration for later use.

Mitigation: Review install commands and run them in an approved environment with least-privilege credential storage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-translate)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu service](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce qhkit JSON responses, credit estimates, task status details, and generated image URLs when executed.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
