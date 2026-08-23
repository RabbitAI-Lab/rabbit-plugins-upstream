## Description:

根据商品图自动生成电商详情页图片套图，整合卖点、场景、参数和营销内容，用于快速制作高转化详情页。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce operators, marketers, and agent users use this skill to create ordered product-detail image sets from a required product reference image, optional theme choices, and optional selling-point copy. The agent can estimate credits, confirm parameters, submit qhkit image jobs, and deliver the generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade Node/npm tooling and modify PATH-related runtime state.

Mitigation: Use a preinstalled qhkit environment when possible and review any package installation or PATH change before execution.

Risk: The skill may reuse local qhkit credentials or ask the user to provide an API key through chat.

Mitigation: Prefer a secure secret store or a user-set QHKIT_TOKEN environment variable, and avoid exposing API keys in conversation history.

Risk: Image generation consumes credits and submitted jobs may not be cancellable.

Mitigation: Run an estimate first and require explicit user confirmation of the model, inputs, theme, and estimated credits before generating.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-detail-page)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key console](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Markdown]

**Output Format:** [Markdown with inline bash commands and JSON CLI payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return ordered image URLs and credit usage from qhkit after user confirmation.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
