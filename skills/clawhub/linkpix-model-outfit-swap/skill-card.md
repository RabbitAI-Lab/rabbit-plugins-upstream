## Description:

上传服装图即可生成真人模特试穿效果，支持不同模特、体型和国家风格，帮助服装卖家快速制作商品展示图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and agents use this skill to turn garment flat-lay or hanger photos into model try-on images, optionally using a supplied model image or a requested model style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the qhkit npm CLI and may install or upgrade local Node.js tooling.

Mitigation: Review package-install behavior for the deployment environment and prefer the documented official npm source and checksum verification steps.

Risk: The workflow requires a Qinghu/LinkPix API key and uploads garment or model images to an external service.

Mitigation: Confirm API key storage practices and avoid uploading sensitive images unless the user accepts the service and data handling requirements.

Risk: Image generation consumes service credits and can produce garment details that differ from the source image.

Mitigation: Estimate credits and obtain explicit user confirmation before generation, then ask the user to inspect logos, text, structure, and other critical product details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-model-outfit-swap)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key tutorial](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Text]

**Output Format:** [Markdown with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs and credit usage from qhkit after user confirmation.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
