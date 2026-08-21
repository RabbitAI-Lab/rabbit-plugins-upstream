## Description:

根据商品图自动生成电商详情页图片套图，整合卖点、场景、参数和营销内容，帮助快速制作高转化详情页。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, merchants, and agents use this skill to generate ordered product detail-page image sets from required product reference images, optional selling-point copy, and selected visual themes through LinkPix/qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and copy may be sent to an external LinkPix/qhkit service.

Mitigation: Tell users before submission and avoid sending sensitive product material unless they approve that external processing.

Risk: The skill may install or upgrade local Node/qhkit tooling and alter the host environment.

Mitigation: Require explicit user approval before installing or upgrading tooling, and report installation failures with the concrete error.

Risk: Existing qhkit credentials may be reused and generation can consume paid credits.

Mitigation: Run a matching estimate when available, present the expected credit cost and key generation parameters, and wait for explicit approval before paid generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-detail-page)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent may produce qhkit commands, cost estimates, status/error summaries, and ordered generated image URLs after user approval.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
