## Description:

LinkFox Amazon Product Selection helps agents research Amazon products, keywords, competitors, reviews, niches, and trends across 33 sub-capabilities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, e-commerce analysts, and developers use this skill to evaluate Amazon product opportunities, compare competitors, analyze keywords, inspect reviews, and track sales or price trends across supported marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles API credentials and can send product research queries, images, and onboarding data to LinkFox services.

Mitigation: Install it only in trusted workspaces, keep credentials in environment variables, and avoid sending confidential business data unless LinkFox is approved for that use.

Risk: Endpoint override variables could route requests to an untrusted host.

Mitigation: Do not set LINKFOX_TOOL_GATEWAY or related endpoint variables unless the destination has been verified.

Risk: Complete API responses are persisted locally under linkfox directories.

Mitigation: Review saved output paths and remove locally stored research data when it is no longer needed.

Risk: Onboarding fallback instructions reference a remote package installation.

Mitigation: Do not allow an agent to auto-install the remote onboarding ZIP without separate verification and approval.

Risk: Repeated calls can consume paid or rate-limited third-party credits.

Mitigation: Ask for user confirmation before retrying, changing parameters, or paginating after empty or failed results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-product-selection)
- [Amazon Product Search](references/linkfox-amazon-search.md)
- [Amazon Search by Image](references/linkfox-amazon-search-by-image.md)
- [Amazon Product Detail Lookup](references/linkfox-amazon-product-detail.md)
- [Amazon Product Reviews](references/linkfox-amazon-reviews-list.md)
- [Amazon Market Opportunity Report](references/linkfox-amazon-opportunity-report-by-keyword.md)
- [Keepa Product Request](references/linkfox-keepa-product-request.md)
- [Jungle Scout Keyword by Keyword](references/linkfox-junglescout-keyword-by-keyword.md)
- [SellerSprite Product Search](references/linkfox-sellersprite-product-search.md)
- [SIF ASIN Keyword Analysis](references/linkfox-sif-asin-keywords.md)
- [Jiimore Niche Info by Keyword](references/linkfox-jiimore-get-niche-info-by-keyword.md)
- [Authentication and Credits](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON request or response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save complete responses under local linkfox directories and may print summaries for large responses unless inline output is requested.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
