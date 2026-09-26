## Description:

京东自营新品首发 helps an agent query JD self-operated new arrivals and filter or sort products by category, price, ratings, subsidy eligibility, trade-in support, and discount strength.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cn-shopping](https://clawhub.ai/user/cn-shopping)

### License/Terms of Use:

MIT-0

## Use Case:

External users and shopping agents use this skill to discover JD self-operated new arrivals, narrow results by keyword or price, and compare discounts and product links before purchase decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shopping search terms, filters, and page parameters are sent to the publisher's Tencent Cloud proxy.

Mitigation: Avoid sensitive personal information in search keywords and review proxy data handling before deployment.

Risk: The artifact includes a shared proxy token for the publisher-operated proxy.

Mitigation: The publisher should rotate the shared token or replace it with a per-deployment secret.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cn-shopping/skills/jd-new-arrivals)
- [Publisher profile](https://clawhub.ai/user/cn-shopping)
- [京东自营超级补贴](https://clawhub.ai/cn-shopping/jd-super-deals)
- [京东自营历史最低价](https://clawhub.ai/cn-shopping/jd-lowest-price)
- [购物比价助手](https://clawhub.ai/cn-shopping/best-price)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [JSON string with content and summary fields; content contains a JSON array of product results when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns paginated product summaries and item fields including prices, discounts, tags, images, and buying links; does not place orders.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
