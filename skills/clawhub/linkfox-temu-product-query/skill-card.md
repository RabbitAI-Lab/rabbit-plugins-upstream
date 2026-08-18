## Description:

Temu商品查询 helps agents search and filter Temu products by keyword, product or store ID, category, price, rating, reviews, sales, listing date, fulfillment mode, region, tags, sorting, and pagination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to query LinkFox's Temu product data service, compare products, and narrow product-selection searches by commercial filters such as price, sales, ratings, fulfillment mode, and region.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Temu search data, session metadata, and full query responses may be sent to LinkFox and stored locally.

Mitigation: Use the skill only with data appropriate for LinkFox processing, and review or remove saved response files when they are no longer needed.

Risk: The onboarding flow uses account credentials, SMS codes, generated API keys, and paid credit purchase flows.

Mitigation: Treat SMS codes and API keys as secrets, configure keys only in trusted environments, and require manual confirmation before selecting plans or completing payment orders.

Risk: Endpoint override environment variables can redirect requests away from the default LinkFox services.

Mitigation: Avoid endpoint overrides unless the destination is controlled and trusted by the user or deploying organization.

## Reference(s):

- [Temu 商品查询 API 参考](artifact/references/api.md)
- [解决认证和积分问题](artifact/references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-product-query)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON parameters, shell commands, configuration snippets, and query-result summaries or saved JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are stored locally by the helper script; small responses may be printed inline, while larger responses are summarized.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
