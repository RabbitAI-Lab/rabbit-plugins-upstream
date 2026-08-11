## Description:

Retrieves structured 1688 product details by offer ID, including title, attributes, SKU pricing and inventory, MOQ, media, logistics, supplier services, invoices, and certificates for sourcing decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sourcing operators and cross-border commerce agents use this skill to look up a known 1688 offer ID or product URL and review SKU price, stock, MOQ, logistics, packaging, supplier, invoice, and certificate facts before procurement decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkFox may receive product lookup requests, API credentials, session or app metadata, and optional feedback content.

Mitigation: Use approved API keys, avoid sending sensitive conversation text through feedback, and install only where this data sharing is acceptable.

Risk: Local response and cache files may retain supplier, pricing, inventory, or logistics data.

Mitigation: Review and clean the local linkfox data and cache directories when that procurement data is sensitive.

Risk: The bundled auth and billing flows can expose generated API keys or payment-related outputs during setup.

Mitigation: Protect generated API keys, share setup output only with authorized users, and verify billing actions before proceeding.

Risk: 1688 product, price, inventory, logistics, and supplier facts are live and may change before purchase.

Mitigation: Reconfirm important facts before procurement and get user confirmation before extra lookups that consume credits.

## Reference(s):

- [1688 Product Detail API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-1688-product-detail)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown summaries and tables backed by JSON API responses or saved JSON response files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may write local JSON response and cache files; live product, price, inventory, logistics, and supplier facts can change.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
