## Description:

面向 POD（Print on Demand）卖家生成设计素材：印花提取、印花贴合（mockup 效果图）、印花裂变、商品效果图，覆盖服饰、家居、饰品等 POD 品类的设计与上架。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

POD sellers and ecommerce operators use this skill to guide agents through LinkPix/qhkit workflows for extracting print artwork, generating design variants, and placing artwork onto product mockups before listing custom merchandise.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead users into qhkit and Node setup, persistent LinkPix API-token configuration, local image uploads to a third-party provider, and paid image-generation steps.

Mitigation: Review the skill before installation, use it only when the LinkPix POD asset workflow is intended, protect API tokens, and require explicit user confirmation before credit-consuming generation.

Risk: Generated POD artwork and mockups can differ from source artwork or involve rights-sensitive designs.

Mitigation: Inspect generated assets for key visual details before use and confirm copyright or brand permissions for commercial POD listings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-assets)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu LinkPix workspace](https://www.iqinghu.com)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to use qhkit image options, estimate, and generate flows; generated images are returned by the external provider when the workflow is executed.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
