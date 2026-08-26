## Description:

根据一张服装模特图自动生成多种姿势及展示角度的套图，丰富商品展示效果，适用于服装详情页及社交媒体营销。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce merchants, marketplace operators, and marketing teams use this skill to turn one fashion model product image into a multi-pose image set for product-detail pages and social media assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The qhkit/LinkPix service reads and uploads user-selected fashion photos to the provider.

Mitigation: Use only images the user intends to send to LinkPix and disclose that submitted paths or URLs are uploaded for generation.

Risk: Generation can consume paid credits.

Mitigation: Run estimate with the exact generation parameters and obtain explicit user approval before submitting paid generation.

Risk: Generated pose-set images may slightly change product details, text, logos, or structure.

Mitigation: Ask the user to review generated outputs for commercially important details before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-model-pose-set)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key console](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit CLI commands, JSON parameters, and generated image URLs when tasks complete]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a configured qhkit token; paid generation should follow estimate output and explicit user approval.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
