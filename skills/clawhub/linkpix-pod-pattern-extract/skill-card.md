## Description:

一键提取图片中的印花图案，生成高清、平铺、可复用的图案素材，适用于 POD 定制及服装设计。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and design-focused agents use this skill to extract print patterns from clothing or product images into reusable POD image assets. It guides setup, model option discovery, credit confirmation, generation, and delivery through the qhkit/LinkPix workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images are uploaded to the qhkit/LinkPix service during image generation.

Mitigation: Use only images the user is allowed to process and make the upload dependency clear before submitting a generation task.

Risk: The workflow uses an API key and may spend account credits after confirmation.

Mitigation: Treat the API key like a password, prefer scoped or temporary credentials where available, and confirm task parameters and estimated credits before running paid generation.

Risk: Generated pattern extraction may not exactly preserve every detail from the source image.

Mitigation: Ask the user to review key visual elements after generation and rerun with clearer region instructions when needed.

Risk: Extracting recognizable brand or IP patterns can create copyright or trademark concerns.

Mitigation: Flag obvious brand or IP content and ask the user to confirm they have appropriate rights before using the output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-extract)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix / iqinghu workspace](https://www.iqinghu.com)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs and credit usage reported by qhkit after user-confirmed generation.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
