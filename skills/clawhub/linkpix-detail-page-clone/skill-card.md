## Description:

智能分析优秀商品详情页设计，用你的商品快速生成同类型布局及视觉风格的详情图，提高详情页制作效率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and e-commerce operators use this skill to guide an agent through generating product detail-page images that approximate the layout and visual style of a provided reference page while using the user's own product images and copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads selected product and reference images to the qhkit/LinkPix provider.

Mitigation: Use only images and brand assets the user is authorized to share with that provider.

Risk: Generate commands may consume paid credits.

Mitigation: Run an estimate when supported and obtain explicit user approval before submitting any generation request.

Risk: The workflow requires a qhkit API token.

Mitigation: Use the provider's token configuration flow or QHKIT_TOKEN environment variable and avoid exposing the token in generated outputs.

Risk: Reference-page cloning is approximate and may accidentally preserve unwanted brand elements or logos.

Mitigation: Keep the prompt constraint to avoid original product, brand, and logo elements, and align expectations before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-detail-page-clone)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key console](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu service homepage](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit image generation, configuration, cost estimation, confirmation, and delivery of generated image URLs.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
