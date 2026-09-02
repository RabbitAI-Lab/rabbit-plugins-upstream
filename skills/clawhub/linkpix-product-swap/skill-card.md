## Description:

一键替换电商图片中的商品主体，并尽量保留原有场景、构图和光影效果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, creative teams, and agents use this skill to replace a product in one or more reference scene images with a new product while preserving the scene composition and lighting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to provide an API token and configure qhkit for a credit-spending service.

Mitigation: Use QHKIT_TOKEN or another secure secret mechanism, avoid pasting tokens into chat, and confirm the active configuration before any generate action.

Risk: Generate actions can upload selected product or scene images to the service and spend account credits.

Mitigation: Run an estimate first, summarize the model, image count, references, and expected credits, and wait for explicit user approval before submitting.

Risk: Generated product swaps may alter details such as logos, text, structure, perspective, or reflections.

Mitigation: Review output images before publication and verify key product details and rights for any reused scene assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-product-swap)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide qhkit calls that upload selected images and spend account credits after user confirmation.]

## Skill Version(s):

0.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
