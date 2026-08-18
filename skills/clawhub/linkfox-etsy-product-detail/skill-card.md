## Description:

Fetches current public details for a single Etsy listing URL, including title, description, prices, currency, images, variants, quantity, category, shipping origin, delivery estimates, shop details, review counts, rating, and aggregate buyer-feedback tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace researchers, ecommerce operators, and agents use this skill to inspect one known Etsy listing for product-page and competitor-page analysis. It is intended for single-listing detail lookup, not Etsy search, bulk screening, seller-account operations, or individual review retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a LinkFox paid-service workflow and may consume credits for each listing lookup.

Mitigation: Tell users before additional paid lookups and avoid automatic retries, changed URLs, or repeated calls unless the user explicitly approves the extra cost.

Risk: Authentication and onboarding flows may involve API keys, phone numbers, SMS verification codes, and payment-order creation.

Mitigation: Use these flows only when the user explicitly requests or needs them, avoid exposing secrets in conversation, and ask the user to confirm any payment action before running it.

Risk: The skill writes lookup responses, cache files, and payment QR artifacts to local disk.

Mitigation: Review local output paths before sharing files and avoid running the skill in workspaces where persisted Etsy or account data should not be stored.

Risk: Public Etsy page changes can cause missing, empty, or misidentified listing fields.

Mitigation: Present returned fields as a current public-page snapshot, preserve unavailable values, and avoid silently repairing or inferring missing shop, price, delivery, or rating data.

Risk: The skill can submit feedback to an external LinkFox feedback API.

Mitigation: Keep feedback concise and avoid including secrets, personal data, or unnecessary listing details when reporting behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-etsy-product-detail)
- [Etsy 商品详情 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses and saved JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The lookup script writes full responses under a local linkfox session directory, uses a 24-hour local cache, and may print either full JSON or a compact summary depending on response size.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
