## Description:

亚马逊选品一站式 AI 工具集，整合 竞品查询/ABA/前台/Keepa/Sorftime/Jungle Scout/卖家精灵/SIF/极目/商业洞察等 12 类工具 33 项子能力，覆盖选品、关键词、竞品、评论、利基与趋势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, analysts, and e-commerce operators use this skill to research Amazon product opportunities, competitors, keywords, reviews, sales trends, and niche-market signals across supported marketplaces. The skill helps an agent choose relevant LinkFox sub-capabilities, make API-backed research calls, and summarize product-selection evidence for business decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends API keys, search queries, ASINs, and image URLs to LinkFox services through an environment-configurable gateway.

Mitigation: Use the skill only in a trusted environment, keep LINKFOX_TOOL_GATEWAY unset or pointed at a trusted LinkFox host, and avoid submitting sensitive research inputs unless the user approves.

Risk: Full API responses may be written to local linkfox data and cache directories, which can retain sensitive product research output.

Mitigation: Review where outputs are written and clear the local linkfox data/cache directories when research results should not persist.

Risk: Registration, API-key generation, and payment order creation can have account or billing impact.

Mitigation: Treat account setup, API-key generation, and payment order creation as explicit user-approved steps only.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-product-selection)
- [Skill definition](artifact/SKILL.md)
- [Onboarding](artifact/references/onboarding.md)
- [ABA intelligent query](artifact/references/linkfox-aba-intelligent-query.md)
- [Amazon search](artifact/references/linkfox-amazon-search.md)
- [Amazon search by image](artifact/references/linkfox-amazon-search-by-image.md)
- [Amazon product detail](artifact/references/linkfox-amazon-product-detail.md)
- [Amazon reviews list](artifact/references/linkfox-amazon-reviews-list.md)
- [Amazon opportunity report by keyword](artifact/references/linkfox-amazon-opportunity-report-by-keyword.md)
- [Amazon opportunity search by metrics](artifact/references/linkfox-amazon-opportunity-search-by-metrics.md)
- [Keepa product request](artifact/references/linkfox-keepa-product-request.md)
- [Keepa product search](artifact/references/linkfox-keepa-product-search.md)
- [Jungle Scout product database](artifact/references/linkfox-junglescout-product-database.md)
- [Jungle Scout keyword by keyword](artifact/references/linkfox-junglescout-keyword-by-keyword.md)
- [SellerSprite product search](artifact/references/linkfox-sellersprite-product-search.md)
- [SellerSprite competitor lookup](artifact/references/linkfox-sellersprite-competitor-lookup.md)
- [SIF ASIN keywords](artifact/references/linkfox-sif-asin-keywords.md)
- [SIF keyword overview](artifact/references/linkfox-sif-keyword-overview.md)
- [Jiimore niche info by keyword](artifact/references/linkfox-jiimore-get-niche-info-by-keyword.md)
- [Jiimore product discovery](artifact/references/linkfox-jiimore-product-discovery.md)
- [Sorftime Amazon product detail](artifact/references/linkfox-sorftime-amazon-product-detail.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request examples, shell commands, and saved JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts write full API responses to local linkfox data/cache directories and may print summaries for large responses.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
