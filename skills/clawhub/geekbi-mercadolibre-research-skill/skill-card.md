## Description:

Uses GeekBI to query and combine Mercado Libre product, store, category, and review data for cross-border product selection, market research, competitor analysis, price-band research, sales analysis, and reputation research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and market researchers use this skill to analyze Mercado Libre opportunities with GeekBI-returned product, store, category, and review data. The skill is suited to scoped product-selection and competitor-research questions where conclusions must state the site, filters, sample size, data limits, risks, confidence, and next validation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill authenticates to GeekBI and stores bearer-token login state locally.

Mitigation: Install only when GeekBI is trusted, avoid running it from shared or published repositories, and clear any .geekbi/agent-auth.json copies when work is complete.

Risk: The query scripts support a configurable API destination.

Mitigation: Use the default GeekBI API endpoint and avoid custom --base-url values unless the destination is explicitly trusted.

Risk: Market conclusions can be overstated when based on limited product, store, review, or category samples.

Mitigation: State the site, filters, page window, actual sample size, data limits, update time, confidence, and next validation steps in the output.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-mercadolibre-research-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-mercadolibre-research-skill)
- [GeekBI API endpoint](https://openapi.geekbi.com)
- [Mercado Libre Seller Reputation](https://global-selling.mercadolibre.com/devsite/en_us/price-per-variation-cbt/seller-reputation-global-selling)
- [Mercado Libre User Products](https://global-selling.mercadolibre.com/devsite/en_us/deals-gs/user-products-cbt)
- [Mercado Libre Global Listing](https://global-selling.mercadolibre.com/devsite/en_us/sync-and-modify-listings-gs/global-listing)
- [Mercado Libre Fully Managed](https://global-selling.mercadolibre.com/devsite/en_us/manage-claims/fully-managed-product-publishing)
- [Mercado Libre product interface](references/MercadoLibre商品接口.md)
- [Mercado Libre operations and policy scope](references/MercadoLibre运营与政策口径.md)
- [Query pause and resume flow](references/查询暂停与恢复流程.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown business analysis with data scope, key evidence, opportunities, risks, confidence, and next validation steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill should avoid exposing raw JSON, access tokens, device codes, authorization headers, or internal authentication objects in user-facing output.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
