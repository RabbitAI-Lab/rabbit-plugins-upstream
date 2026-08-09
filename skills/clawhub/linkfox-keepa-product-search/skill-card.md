## Description:

基于Keepa数据的亚马逊高级商品搜索与筛选，支持品类、价格、月销量、关键词、BSR排名、评论数、评分、包装尺寸、重量、配送方式等多维度条件。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, e-commerce operators, and agents use this skill to build multi-criteria Keepa product searches, call the LinkFox Keepa search endpoint, and present product research results with sales, price, BSR, rating, review, fulfillment, and package filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends search parameters and an API key to LinkFox services.

Mitigation: Use only approved LinkFox credentials, avoid including unnecessary sensitive business data in search parameters, and review endpoint access before use.

Risk: The skill can guide users through account setup, API-key creation, and payment flows.

Mitigation: Prefer self-service setup in LinkFox, and do not hand an agent SMS codes, payment choices, or other account recovery details unless that workflow is explicitly approved.

Risk: Full API responses are written to local session files.

Mitigation: Review and remove saved response files when they contain sensitive product research data, credentials, or account-related information.

Risk: Keepa searches can consume paid LinkFox credits.

Mitigation: Confirm cost-bearing searches before additional pages, history-enabled requests, or modified retry queries.

## Reference(s):

- [Keepa product search API reference](references/api.md)
- [LinkFox authentication and billing onboarding](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-keepa-product-search)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, API calls, files, guidance]

**Output Format:** [Markdown guidance with inline shell commands and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are persisted under a local linkfox session directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
