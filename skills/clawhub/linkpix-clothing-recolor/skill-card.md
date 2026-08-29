## Description:

一键生成服装的不同颜色版本，保持版型、材质及光影一致，无需重新拍摄即可完成 SKU 色卡图制作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce operators, designers, and agents use this skill to create alternate clothing color images and SKU color-card variants from an existing garment image while preserving style, texture, and lighting as much as the generation model allows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade local Node tooling and the qhkit package.

Mitigation: Review the package installation step and run it in an environment where tool changes are acceptable.

Risk: The workflow may persist or use an API token for LinkPix/qhkit.

Mitigation: Configure the token through a secure secret mechanism when available and avoid exposing it in chat or logs.

Risk: Uploaded garment images are sent to qhkit/LinkPix for generation.

Mitigation: Use the skill only with images that are approved for processing by the external service.

Risk: Broad trigger wording could cause the skill to be invoked for unrelated color edits.

Mitigation: Limit use to clothing recolor and SKU color-card workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-clothing-recolor)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [LinkPix API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON command arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit image generation workflows that may return generated image URLs and credit usage.]

## Skill Version(s):

0.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
