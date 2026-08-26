## Description:

一键生成服装的不同颜色版本，保持版型、材质及光影一致，无需重新拍摄即可完成 SKU 色卡图制作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, catalog operators, and agents use this skill to create alternate color images for clothing SKUs from an existing product image while preserving fit, material texture, lighting, and key product details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends clothing or product images, prompts, and an API key to the qhkit/Qinghu service.

Mitigation: Use the skill only when the user is comfortable sharing those inputs with that service, and configure credentials through the documented qhkit token or environment variable path.

Risk: Image generation can consume account credits and cannot be cancelled after task submission.

Mitigation: Before generation, show the selected model, image count, size, reference images, and estimated credits, then wait for explicit user approval.

Risk: Generated recolors are not pixel-level edits and may alter logos, text, structure, or other product details.

Mitigation: Ask the user to review key product details after generation and include prompt constraints such as keeping logos or printed patterns unchanged when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-clothing-recolor)
- [autoagc publisher profile](https://clawhub.ai/user/autoagc)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu account and console](https://www.iqinghu.com)
- [Qinghu API keys page](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent queries current model and size options, estimates credits before paid generation, waits for explicit user approval, and returns generated image URLs with actual credit use.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
