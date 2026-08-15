## Description:

Retrieves structured Amazon product detail data by ASIN, including listing text, images, price, ratings, reviews, variants, specifications, A+ content, and optional related-product data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, Amazon sellers, ecommerce researchers, and developers use this skill to fetch and compare current Amazon product page data across supported marketplaces from one or more ASINs. It supports listing analysis workflows such as extracting bullet points, specifications, prices, ratings, reviews, images, variants, and A+ content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a LinkFox API key and sends ASIN query data to LinkFox services.

Mitigation: Install only when that data sharing is acceptable, provide API keys through the documented environment variables, and avoid pasting credentials into conversation text.

Risk: Lookup calls consume account credits and batch requests can multiply cost by the number of returned products.

Mitigation: Confirm the needed ASINs before querying, keep batches limited to products the user intentionally requests, and avoid automatic retry or exploratory follow-up calls that create extra charges.

Risk: The skill includes account onboarding and payment helper flows for authentication and balance issues.

Mitigation: Use phone/SMS onboarding, plan selection, and recharge commands only after explicit user intent, and show returned payment or account setup details without polling or continuing on the user's behalf.

Risk: Full lookup responses are stored locally and may include detailed product and query context.

Mitigation: Review saved response files before sharing them outside the workspace and delete session data when it is no longer needed.

Risk: Automatic feedback reporting can include sensitive conversation details if used carelessly.

Mitigation: Do not submit feedback that contains secrets, personal data, or sensitive business context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-product-detail)
- [Amazon product detail API reference](artifact/references/api.md)
- [Authentication and billing onboarding guide](artifact/references/onboarding.md)
- [LinkFox skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell commands, and JSON API responses or response summaries written to local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The lookup script stores full responses under a local linkfox session directory, uses a 24-hour cache for repeated parameter combinations, prints small responses inline, and summarizes larger responses unless --inline is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
