## Description:

极鲸云 Temu 图搜同款/商品图片搜索 uploads a user-selected product image to GeekBI, searches Temu for visually similar product candidates, and helps analyze market performance and competition using returned product data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External cross-border sellers and sourcing teams use this skill to search Temu visual matches from supplier, product, screenshot, or uploaded images, then compare candidate sales, prices, supply prices, listing age, ratings, and same-item competition. The skill is useful for building candidate lists, evaluating product opportunities, and deciding what needs further specification or supplier validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images or image URLs are sent to GeekBI for Temu visual search.

Mitigation: Use only images that are appropriate to share with GeekBI; avoid private, internal, embargoed, or otherwise sensitive product images and URLs.

Risk: GeekBI authentication state may be reused across GeekBI Temu skills.

Mitigation: Clear GeekBI auth state when shared login reuse is no longer desired, and do not expose tokens, device codes, request headers, or auth-state files in conversations or logs.

Risk: Visual matches may be similar without proving identical specifications, materials, dimensions, functionality, or supply chain.

Mitigation: Treat results as visual candidates and require follow-up verification before sourcing, pricing, or product-launch decisions.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-temu-image-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-temu-image-search-skill)
- [Publisher profile](https://clawhub.ai/user/geekbi)
- [Temu 图搜同款](references/Temu图搜同款.md)
- [Temu 图搜同款接口](references/Temu图搜同款接口.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)
- [GeekBI OpenAPI endpoint](https://openapi.geekbi.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, API calls, guidance]

**Output Format:** [Chinese Markdown summaries with linked product titles and occasional JSON or shell-command output when explicitly requested for troubleshooting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs distinguish visual-match facts, returned product-data facts, and business judgment; product links use server-returned linkUrl values.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
