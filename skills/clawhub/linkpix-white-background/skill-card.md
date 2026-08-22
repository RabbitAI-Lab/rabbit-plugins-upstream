## Description:

LinkPix 批量将商品图片处理为干净的纯白背景图，自动识别商品主体并移除杂乱背景以适配电商平台主图规范。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, operators, and agents use this skill to prepare product photos for marketplace white-background listing requirements, including batch processing with qhkit/LinkPix. It helps confirm generation parameters, estimate credits when available, submit approved image jobs, and deliver generated image URLs with credit usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or upgrade qhkit/Node tooling and reuse local service credentials.

Mitigation: Prefer a pre-provisioned or sandboxed qhkit environment; avoid global upgrades, system-path Node installation, and privileged token reuse unless intended for the environment.

Risk: Generate calls upload selected product images and spend service credits.

Mitigation: List the model, prompt template, image count, dimensions, reference images, and estimated credits when available, then wait for explicit user approval before submitting generate jobs.

Risk: The white-background result is a generative edit rather than pixel-level masking, so product details may change.

Mitigation: Ask the user to inspect important details such as text, logos, and product structure before publishing the generated image.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-white-background)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Image URLs]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command results; generated outputs are white-background JPG/PNG image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generate calls can upload selected product images and spend qhkit/LinkPix credits after explicit user confirmation.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
