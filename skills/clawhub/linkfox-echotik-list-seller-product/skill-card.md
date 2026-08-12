## Description:

Lists products for a single TikTok Shop seller by sellerId and returns product titles, prices, sales and GMV windows, ratings, reviews, commission rates, listing dates, sales channels, and categories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and ecommerce analysts use this skill to inspect what a known TikTok Shop store sells and compare per-product price, sales, GMV, review, category, and commission metrics. Developers and agent operators can also use it to retrieve the underlying EchoTik seller-product response for downstream reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires LinkFox/EchoTik API credentials and includes account setup, API-key generation, billing, and payment-order flows.

Mitigation: Review any phone-code, API-key, billing, or payment-order step before allowing the agent to run it.

Risk: Full API responses and QR images may be saved under a local linkfox directory.

Mitigation: Inspect saved files for sensitive account or business data and delete them when they are no longer needed.

Risk: Repeated product-list calls can consume paid credits.

Mitigation: Confirm with the user before pagination, repeated calls, or high-frequency use when credit cost is unclear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-list-seller-product)
- [EchoTik seller product API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown summaries, shell commands, and JSON responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a sellerId, may consume LinkFox credits, caches identical calls for 24 hours, and saves full API responses under a local linkfox directory.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
