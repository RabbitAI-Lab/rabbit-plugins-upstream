## Description:

This skill uses GeekBI to query and analyze real Ozon product reviews for a confirmed goodsId, including ratings, text, pros and cons, specifications, media indicators, helpful votes, seller replies, and review timestamps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace sellers, analysts, and agents use this skill to research Ozon product reputation, selling points, negative review drivers, specification risks, and improvement opportunities from returned review data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports that the skill stores GeekBI login state locally in multiple locations.

Mitigation: Use only workspaces and accounts where local GeekBI login-state storage is acceptable, confirm storage isolation before sensitive use, and clear auth state in shared environments.

Risk: ClawScan reports undocumented API-origin overrides alongside GeekBI API access.

Mitigation: Restrict API and authentication URLs to approved HTTPS GeekBI hosts before using the skill with sensitive accounts or data.

Risk: Returned Ozon reviews are a bounded sample and may not represent all platform reviews or official operating metrics.

Mitigation: Report the queried parameters, returned totals, read count, pages, rating criteria, and time range, and avoid claiming official quality, complaint, return, or profit rates from the sample.

Risk: Authentication or quota actions can interrupt review queries.

Mitigation: When actionRequired is returned, pause analysis, show only the user-facing prompt and valid action link, then rerun the original query only after the user confirms completion.

## Reference(s):

- [Server-resolved GitHub repository](https://github.com/geekbi/geekbi-ozon-review-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-ozon-review-search-skill)
- [Ozon review API reference](references/Ozon评论接口.md)
- [Ozon review research guidance](references/Ozon评论研究.md)
- [Query pause and resume process](references/查询暂停与恢复流程.md)
- [Ozon operations and policy guidance](references/Ozon运营与政策口径.md)
- [Ozon Partner Delivery](https://docs.ozon.com/global/en/fulfillment/rfbs/logistic-settings/partner-delivery-ozon/?country=TR)
- [Ozon Analytics Tools](https://docs.ozon.com/global/tr/analytics/analytics-and-metrics/analytics-tools/?country=TR)
- [Ozon product and price management](https://docs.ozon.com/global/ozon-seller-app/product-management/)
- [Ozon promotions](https://docs.ozon.com/global/promotion/promotions/promo/?country=OTHER)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown analysis with JSON results from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a confirmed goodsId; defaults to the Russia site when no site is specified and limits review access to the first 200 returned reviews.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
