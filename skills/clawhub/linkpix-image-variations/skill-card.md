## Description:

基于一张商品图快速生成多种营销版本，支持不同背景、布局和设计风格，帮助量产广告素材。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, marketers, and their agents use this skill to create multiple product-image variants from one source image for campaign production and A/B testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or upgrade Node and qhkit on the host.

Mitigation: Use a controlled environment where dependency installation and upgrades are explicitly approved.

Risk: The skill uploads referenced images to the LinkPix/qhkit service.

Mitigation: Use only product images that are appropriate for upload to that service.

Risk: Image generation can consume account credits.

Mitigation: Run an estimate when supported and obtain explicit user approval of model, image count, size, reference images, and estimated credits before submitting generation.

Risk: The skill may reuse an existing OpenClaw qinghu credential file.

Mitigation: Review credential scope and avoid running the skill with shared or overly privileged credentials.

Risk: Generated product variants can change details such as text, logos, or product structure.

Mitigation: Review generated images for brand, text, and product-accuracy issues before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-variations)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON command arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs and actual credit usage returned by qhkit.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
