## Description:

智能识别商品主体并将商品图背景替换为不同风格的营销场景图，无需 PS。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, marketers, and agents use this skill to turn product images into background-swapped marketing scene images through the LinkPix/qhkit workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images are uploaded to the qhkit/LinkPix service for background replacement.

Mitigation: Use the skill only when the user is comfortable sharing the images with that service and avoid processing sensitive product imagery without approval.

Risk: The qhkit workflow can store or use a local API token.

Mitigation: Use an approved qhkit token, keep it out of chat logs and generated files, and rely on the documented config or QHKIT_TOKEN paths.

Risk: Image generation can consume service credits after submission.

Mitigation: Run an estimate when supported, summarize the expected cost and key parameters, and wait for explicit user confirmation before generation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-background-swap)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API Keys Dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided product images, a configured qhkit token, and explicit approval before paid generation.]

## Skill Version(s):

0.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
