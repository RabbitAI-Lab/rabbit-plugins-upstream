## Description:

Queries a single TikTok Shop seller by sellerId and returns a detailed store profile with sales, GMV, follower, rating, fulfillment, product, category, video, influencer, livestream, and listing-date metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, analysts, and marketers use this skill to inspect one known TikTok Shop store's performance profile by sellerId. It is useful for benchmarking a store's sales momentum, GMV, followers, ratings, fulfillment indicators, content reach, and product mix.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Seller lookup requests, API keys, and session metadata are sent to LinkFox/EchoTik services.

Mitigation: Use the skill only when that data sharing is acceptable, and prefer obtaining and storing the API key yourself through the official LinkFox site.

Risk: The bundled onboarding flow can handle phone/SMS login, API-key creation, package listing, and payment-order creation.

Mitigation: Do not run onboarding login or payment commands unless the user explicitly intends to provide a phone/SMS code or create a payment order.

Risk: Full API responses are persisted to local linkfox folders.

Mitigation: Review the saved response location and avoid running the skill from workspaces where persisted seller data or account metadata would be inappropriate.

Risk: Each seller-detail lookup consumes LinkFox credits.

Mitigation: Confirm user intent before repeated calls, especially when the user may not expect additional credit consumption.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-seller-detail)
- [EchoTik-TikTok店铺详情 API 参考](artifact/references/api.md)
- [解决认证和积分问题](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API results and local JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires sellerId; full responses are written under a local linkfox session directory, with stdout showing full JSON for small responses or a summary for larger responses.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
