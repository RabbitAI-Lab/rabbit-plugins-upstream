## Description:

爆款复刻。上传商品原图 + 亚马逊 listing 链接/ASIN 或爆款参考图，自动将参考图的排版与风格套用到你的商品上批量生成新图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and operators use this skill to turn a product image plus an Amazon listing, ASIN, or uploaded reference images into a batch of marketplace-style replica product images. It is aimed at comparing successful listing visuals and producing a reference-to-result image table for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product or reference images may be uploaded to public URLs.

Mitigation: Use only images whose public exposure is acceptable, and avoid sensitive or proprietary product imagery unless release terms allow it.

Risk: The workflow can use paid external LinkFox APIs and credentials.

Mitigation: Run it in a clean environment with trusted LINKFOX_* endpoint variables, least-privilege credentials, and billing expectations reviewed before use.

Risk: Amazon listing data and generated images may be persisted locally.

Mitigation: Review generated files and remove local response data after use when working with confidential campaigns or customer assets.

## Reference(s):

- [Workflow](references/workflow.md)
- [Data Fields](references/data-fields.md)
- [AI Image Generation API](skills/linkfox-aigc-imagegen/references/api.md)
- [Amazon Product Detail API](skills/linkfox-amazon-product-detail/references/api.md)
- [File Upload API](skills/linkfox-file-upload/references/api.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-aigc-imagegen-bestseller-replicate)

## Skill Output:

**Output Type(s):** [Files, Markdown, Guidance]

**Output Format:** [Markdown comparison table with generated image file paths and failure notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one replica image per reference image when generation succeeds; failed references are reported separately.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
