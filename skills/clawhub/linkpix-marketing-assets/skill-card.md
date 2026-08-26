## Description:

一站式生成电商营销素材：商品主图、场景图、详情页、促销海报、广告图片与广告视频，覆盖商品包装、活动推广和品牌营销。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce operators use this skill to plan and generate product marketing assets, including main images, scene images, detail pages, promotional posters, ad images, and ad videos through qhkit workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may install or upgrade qhkit and supporting runtimes.

Mitigation: Review installation prompts and prefer the documented npm package and checksum-verified Node installation path before continuing.

Risk: Selected product media may be uploaded to the qhkit service during generation.

Mitigation: Use only files intended for the marketing task and avoid providing unrelated private or sensitive media as references.

Risk: Generate actions may spend account credits.

Mitigation: Run estimates where supported and require explicit user confirmation of model, asset count, media inputs, and expected credits before submitting generation jobs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-marketing-assets)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQingHu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated media URLs returned by qhkit and credit usage reported by the service.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
