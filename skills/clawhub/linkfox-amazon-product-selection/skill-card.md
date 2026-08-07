## Description:

亚马逊选品一站式 AI 工具集，整合竞品查询、ABA、前台、Keepa、Sorftime、Jungle Scout、卖家精灵、SIF、极目和商业洞察等能力，覆盖选品、关键词、竞品、评论、利基与趋势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, e-commerce operators, and market researchers use this skill to select products, research markets, analyze competitors, inspect keywords, review customer feedback, track historical trends, and screen niches across supported Amazon marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys and query data are sent to LinkFox services.

Mitigation: Use the skill only in environments where sharing those credentials and query contents with LinkFox services is acceptable.

Risk: Network requests can use a configurable LINKFOX_TOOL_GATEWAY value.

Mitigation: Run with the default or another trusted gateway value and review environment configuration before execution.

Risk: Full query results and cache files may remain on disk.

Mitigation: Run in an appropriate workspace, avoid sensitive product or account data where possible, and delete generated result or cache files when they are no longer needed.

Risk: The onboarding flow can involve account and payment actions.

Mitigation: Review onboarding prompts and billing choices before running account or payment commands.

Risk: Remote fallback skill installation instructions may fetch code outside the packaged artifact.

Mitigation: Verify any remote package URL and contents separately before installing or executing fetched code.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-product-selection)
- [LinkFox publisher profile](https://clawhub.ai/user/linkfox-ai)
- [Linkfox ABA Intelligent Query](references/linkfox-aba-intelligent-query.md)
- [Linkfox Amazon Alexa Search](references/linkfox-amazon-alexa-search.md)
- [Linkfox Amazon Opportunity Report by Keyword](references/linkfox-amazon-opportunity-report-by-keyword.md)
- [Linkfox Amazon Opportunity Search by Metrics](references/linkfox-amazon-opportunity-search-by-metrics.md)
- [Linkfox Amazon Product Detail](references/linkfox-amazon-product-detail.md)
- [Linkfox Amazon Reviews List](references/linkfox-amazon-reviews-list.md)
- [Linkfox Amazon Search](references/linkfox-amazon-search.md)
- [Linkfox Amazon Search by Image](references/linkfox-amazon-search-by-image.md)
- [Linkfox Jiimore Niche Info](references/linkfox-jiimore-get-niche-info.md)
- [Linkfox Jiimore Niche Info by Keyword](references/linkfox-jiimore-get-niche-info-by-keyword.md)
- [Linkfox Jiimore Niche Review from Keyword](references/linkfox-jiimore-get-niche-review-from-keyword.md)
- [Linkfox Jiimore Page ASINs by ASIN](references/linkfox-jiimore-page-asins-by-asin.md)
- [Linkfox Jiimore Product Discovery](references/linkfox-jiimore-product-discovery.md)
- [Linkfox Jungle Scout Keyword by ASIN](references/linkfox-junglescout-keyword-by-asin.md)
- [Linkfox Jungle Scout Keyword by Keyword](references/linkfox-junglescout-keyword-by-keyword.md)
- [Linkfox Jungle Scout Keyword History](references/linkfox-junglescout-keyword-history.md)
- [Linkfox Jungle Scout Keyword Share of Voice](references/linkfox-junglescout-keyword-share-of-voice.md)
- [Linkfox Jungle Scout Product Database](references/linkfox-junglescout-product-database.md)
- [Linkfox Jungle Scout Sales Estimates](references/linkfox-junglescout-sales-estimates.md)
- [Linkfox Keepa Product Request](references/linkfox-keepa-product-request.md)
- [Linkfox Keepa Product Search](references/linkfox-keepa-product-search.md)
- [Linkfox Keepa Product Series](references/linkfox-keepa-product-series.md)
- [Linkfox SellerSprite Competitor Lookup](references/linkfox-sellersprite-competitor-lookup.md)
- [Linkfox SellerSprite Market Research](references/linkfox-sellersprite-market-research.md)
- [Linkfox SellerSprite Market Statistics](references/linkfox-sellersprite-market-statistics.md)
- [Linkfox SellerSprite Product Search](references/linkfox-sellersprite-product-search.md)
- [Linkfox SellerSprite Traffic Keyword](references/linkfox-sellersprite-traffic-keyword.md)
- [Linkfox SIF ASIN Keywords](references/linkfox-sif-asin-keywords.md)
- [Linkfox SIF ASIN Summary](references/linkfox-sif-asin-summary.md)
- [Linkfox SIF Keyword Overview](references/linkfox-sif-keyword-overview.md)
- [Linkfox SIF Keyword Summary](references/linkfox-sif-keyword-summary.md)
- [Linkfox Sorftime Amazon Product Detail](references/linkfox-sorftime-amazon-product-detail.md)
- [Linkfox Sorftime Amazon Product Query](references/linkfox-sorftime-amazon-product-query.md)
- [Linkfox onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance plus JSON API responses and saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a LinkFox API key; scripts may cache responses for 24 hours and persist full query results under the working directory.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
