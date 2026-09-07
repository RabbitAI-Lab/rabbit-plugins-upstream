## Description:

This skill uses GeekBI to search and analyze real Mercado Libre product reviews for a specified item or product ID, including ratings, review text, image links, helpfulness counts, and review timestamps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, analysts, and operators use this skill to inspect Mercado Libre review data for a known product or item ID, summarize review scope and ratings, identify praised selling points and pain points, and propose product improvement or validation actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authoritative security review reports that login tokens may be stored in multiple local locations.

Mitigation: After use, run `python3 scripts/geekbi_auth.py clear` and check for leftover `.geekbi/agent-auth.json` copies when credential exposure matters.

Risk: The authoritative security review reports an unrestricted API origin option.

Mitigation: Use the default GeekBI API origin, `https://openapi.geekbi.com`, and avoid passing custom base URLs unless they have been reviewed.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-mercadolibre-review-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-mercadolibre-review-search-skill)
- [Mercado Libre 评论接口](references/MercadoLibre评论接口.md)
- [Mercado Libre 评论研究](references/MercadoLibre评论研究.md)
- [Mercado Libre 运营与政策口径](references/MercadoLibre运营与政策口径.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)
- [Mercado Libre Seller Reputation](https://global-selling.mercadolibre.com/devsite/en_us/price-per-variation-cbt/seller-reputation-global-selling)
- [Mercado Libre User Products](https://global-selling.mercadolibre.com/devsite/en_us/deals-gs/user-products-cbt)
- [Mercado Libre Global Listing](https://global-selling.mercadolibre.com/devsite/en_us/sync-and-modify-listings-gs/global-listing)
- [Mercado Libre Fully Managed](https://global-selling.mercadolibre.com/devsite/en_us/manage-claims/fully-managed-product-publishing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown analysis with referenced shell commands and JSON-backed findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default analysis includes a one-sentence conclusion, data scope, rating and theme summary, praised points, pain points, and improvement or validation actions.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
