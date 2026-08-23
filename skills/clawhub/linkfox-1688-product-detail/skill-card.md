## Description:

Retrieves a structured 1688 product detail record by offer ID, including title, attributes, SKU pricing and stock, quantity tiers, media, logistics, supplier metrics, invoices, and certificates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sourcing and procurement users use this skill to inspect a known 1688 offer ID or product URL before quoting, buying, or comparing supplier terms. It helps agents summarize product facts, SKU prices and stock, MOQ, logistics details, supplier metrics, and procurement terms without searching for new products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys, account login, phone/SMS onboarding, and account information.

Mitigation: Install only if LinkFox is trusted for those credentials and account flows; prefer self-service account setup and keep API keys in local environment variables rather than sharing them in chat.

Risk: The onboarding helper can list paid plans, create payment orders, and render payment QR codes.

Mitigation: Review the selected plan, payment method, amount, and QR or payment URL before paying; do not create orders unless the user explicitly chooses a plan.

Risk: The lookup script persists product and supplier responses in local LinkFox session and cache directories.

Mitigation: Delete local LinkFox response and cache directories when retained sourcing data should not persist, and avoid running the skill from sensitive shared workspaces.

Risk: Product price, stock, logistics, and supplier data are live and may change after a cached lookup.

Mitigation: Use real-time lookup for price-sensitive decisions and reconfirm final purchase cost with an order preview before buying.

Risk: Gateway and feedback endpoints can receive product lookup requests and quality feedback.

Mitigation: Avoid sending sensitive business context in lookup parameters or feedback content, and keep LinkFox gateway environment variables pointed only at trusted hosts.

## Reference(s):

- [1688 Product Detail API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-1688-product-detail)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration guidance]

**Output Format:** [JSON API responses with concise Markdown summaries and inline shell commands for setup or billing recovery.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The lookup script saves full responses to a local LinkFox session directory, may use a 24-hour cache unless real-time lookup is requested, and summarizes large responses on stdout.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
