## Description:

通过极鲸云上传商品图片并搜索 Temu 视觉相似商品，支持按站点和商品指标筛选候选，并基于真实返回结果分析市场表现与竞争。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External cross-border sellers and analysts use this skill to search Temu for visually similar products from a supplied product image, then review sales, price, supply price, launch timing, rating, and similarity-count signals to assess market opportunity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided product images, image URLs, and query parameters are sent to GeekBI for processing.

Mitigation: Use only images and URLs the user is authorized to share; avoid confidential, personal, customer, or private-network material.

Risk: GeekBI login state may be stored locally and reused by related skills.

Mitigation: Run the skill only in environments where local credential storage and account reuse are acceptable.

Risk: Visual matches are candidate products and do not prove identical specifications, materials, functions, or suppliers.

Mitigation: Treat results as visually similar candidates and require follow-up verification before sourcing or market decisions.

## Reference(s):

- [Temu 图搜同款](references/Temu图搜同款.md)
- [Temu 图搜同款接口](references/Temu图搜同款接口.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)
- [Source repository](https://github.com/geekbi/geekbi-temu-image-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-temu-image-search-skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown with linked product titles, concise business analysis, and occasional shell commands for skill execution.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Grounded in GeekBI service results; raw JSON is shown only when requested for troubleshooting or integration.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
