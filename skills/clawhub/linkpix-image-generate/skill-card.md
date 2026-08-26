## Description:

按文字描述直出商业级电商图片，支持可选参考图（图生图/改图），自定义生图家族实时清单可选（智慧模型/图片5.0 Pro/图片5.0 Lite/专图模型等）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce content teams use this skill to guide an agent through LinkPix image generation, prompt polishing, reference-image workflows, model selection, cost estimation, and delivery of generated product or scene images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires installing and using the qhkit npm CLI.

Mitigation: Install only in environments where use of the qhkit CLI is approved, and follow the skill's package and checksum guidance when bootstrapping dependencies.

Risk: Prompts and reference images may be sent to the Qinghu/LinkPix service.

Mitigation: Use only content the user is permitted to transmit to the service, and confirm sensitive or proprietary image handling expectations before generation.

Risk: Image generation consumes service credits.

Mitigation: Run an estimate first and confirm the model, image count, quality, size, reference files, and estimated credits before submitting generation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-image-generate)
- [qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu Account and Console](https://www.iqinghu.com)
- [Qinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API Key Setup Guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may guide an agent to run qhkit commands that return JSON status, estimates, and generated image URLs.]

## Skill Version(s):

0.1.3 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
