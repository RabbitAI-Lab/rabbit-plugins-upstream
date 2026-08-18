## Description:

Searches and analyzes product listings on China's 1688 wholesale platform to help e-commerce sellers compare suppliers, prices, sales metrics, and fulfillment options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers, sourcing professionals, and agents use this skill to find 1688 products and suppliers by keyword, product URL, or product ID, then compare pricing, sales volume, factory status, shipping speed, and dropshipping filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkFox services may handle product search requests, phone/SMS login data, account tokens, and API keys.

Mitigation: Install only when this data handling is acceptable, prefer self-service registration or billing, and avoid sharing or logging generated API keys.

Risk: Search and onboarding flows can consume credits or create payment orders.

Mitigation: Confirm the 9-credit search cost and any billing action with the user before high-frequency searches, plan purchases, or payment order creation.

Risk: Configurable endpoint environment variables can change which LinkFox services receive requests.

Mitigation: Verify LinkFox endpoint environment variables before use and keep them pointed at trusted expected services.

Risk: Automatic feedback reporting may send quality or usage signals about the skill.

Mitigation: Review feedback behavior before deployment and avoid including sensitive user or account data in feedback content.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-dld-product-search)
- [DianLeiDa 1688 product search API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses, saved JSON data files, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Product-search calls consume 9 credits; large API responses are saved as local JSON files and summarized in stdout.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
