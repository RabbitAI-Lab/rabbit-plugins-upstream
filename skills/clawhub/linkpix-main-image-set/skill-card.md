## Description:

智能识别商品主体，根据一张产品图一键生成不同类型、不同电商平台风格的主图+轮播图套图，无需写提示词。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and e-commerce operators use this skill to generate marketplace-ready main product images and carousel image sets from product photos, optional sales copy, and platform preferences. It guides the agent through qhkit setup, option lookup, credit estimation, confirmation, generation, and delivery of resulting image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may require installing a global npm CLI and configuring a Qinghu/LinkPix API key.

Mitigation: Install qhkit only when missing, use the documented npx fallback for permission issues, and configure credentials only after the user provides or confirms the API key.

Risk: Selected product images and copy are uploaded to the LinkPix service for generation.

Mitigation: Use only the assets and copy selected for the task, and install the skill only when the user is comfortable with external upload to the service.

Risk: Image generation can consume paid credits.

Mitigation: Run qhkit estimate with the same parameters before generation, report the estimated credits and key parameters, and wait for explicit user approval before calling generate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-main-image-set)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI parameters; generated results are returned as image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit, a Qinghu/LinkPix API key, user-selected product images or copy, credit estimation, and explicit user confirmation before paid generation.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
