## Description:

使用 Nano Banana 2 制作可用于提案、上新和营销测试的产品图，把商品事实、外观锚点、镜头、布光、材质和渠道比例组织成可验收的商业画面。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create product images for proposals, product launches, ecommerce listings, and marketing tests while preserving product facts, authorized visual anchors, camera direction, lighting, materials, and delivery ratios.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images, product assets, and API keys may be sensitive.

Mitigation: Use only authorized product or brand assets, pass only intended reference images, and store API keys through an environment variable or the documented local configuration path with restricted permissions.

Risk: Generated product imagery can misrepresent product structure, packaging, included accessories, or commercial claims.

Mitigation: Review outputs against the product fact table, label concept images and non-standard props clearly, and keep prompts, task IDs, reference images, and approved versions for review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-2-product-image)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash commands, task IDs, JSON task responses, and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are saved locally; reference-image uploads are limited to user-specified image files.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
