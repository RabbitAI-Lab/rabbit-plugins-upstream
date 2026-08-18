## Description:

Looks up the current public details for one Shopee product URL, including price, discounts, sales, inventory, SKU variants, images, brand, category, shop, and rating data when available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and e-commerce operators use this skill to inspect a known Shopee listing and summarize current public product, pricing, stock, SKU, media, and shop signals. It is not intended for keyword search, bulk screening, historical monitoring, review mining, or seller-account operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid LinkFox-backed lookup and may consume credits for product queries.

Mitigation: Tell the user before repeated or additional paid lookups, rely on the documented one-call behavior for a known product URL, and use the 24-hour cache for identical parameters when available.

Risk: The bundled onboarding flow may ask for phone/SMS login, create or use API keys, list plans, and create unpaid payment orders or QR codes.

Mitigation: Prefer manual account setup and payment through LinkFox's site, keep API keys scoped, and do not proceed with billing or login actions without user confirmation.

Risk: The skill can save complete API responses under local linkfox directories.

Mitigation: Review saved files before sharing them, avoid submitting sensitive product or account context, and clean local response files when they are no longer needed.

Risk: Endpoint override environment variables can redirect the skill's network calls.

Mitigation: Avoid endpoint override environment variables unless the execution environment and destination endpoints are trusted.

## Reference(s):

- [Shopee Product Detail API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with optional shell commands and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The lookup accepts one Shopee productUrl at a time, caches repeated parameter combinations for 24 hours, and may save complete API responses under a local linkfox directory.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
