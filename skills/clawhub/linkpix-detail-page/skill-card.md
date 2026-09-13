## Description:

根据商品图自动生成详情页图片套图，整合卖点、场景、参数及营销内容，快速制作高转化详情页。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and agents use this skill to create ordered product-detail image sets from a required product reference image, optional theme, and optional selling-point copy for listing launches or detail-page refreshes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade mutable third-party npm code for qhkit.

Mitigation: Review qhkit before use, pin a reviewed version, and run it in a sandboxed environment instead of relying on global install, npx, or @latest upgrades.

Risk: Product images and related assets are uploaded to an external service.

Mitigation: Use only assets approved for external processing and avoid submitting sensitive, confidential, or regulated product material.

Risk: The workflow uses an API token and may spend service credits.

Mitigation: Use a narrowly scoped token, keep it out of shared logs or files, run estimates before generation, and confirm available balance before spending credits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-detail-page)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Image URLs]

**Output Format:** [Markdown with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates ordered image URL results through qhkit and reports actual credit usage when generation completes.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
