## Description:

Shopee global product management skill for authorized merchants, covering Shopee Open Platform GlobalProduct APIs for category lookup, global item and SKU management, publishing, price, and stock updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee merchants and ecommerce operators use this skill to query, create, update, publish, and manage cross-border GlobalProduct listings through LinkFox-assisted Shopee API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can affect Shopee merchant catalog state through price, stock, publish, update, and delete operations.

Mitigation: Require explicit user confirmation before any price, stock, publish, update, or delete action.

Risk: The skill handles LinkFox credentials, SMS verification, generated API keys, and Shopee merchant data.

Mitigation: Use only trusted credential channels, install only if LinkFox is trusted with this data, and avoid exposing API keys in shared logs or prompts.

Risk: The skill persists full LinkFox responses and payment or QR-related outputs in local session files.

Mitigation: Periodically review and remove locally saved LinkFox response and QR files that may contain sensitive business or payment data.

Risk: Environment URL overrides could route requests away from the expected LinkFox gateway.

Mitigation: Avoid environment URL overrides unless the endpoint is independently trusted and intentionally configured.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-global-product)
- [GlobalProduct API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [Shopee Open Platform GlobalProduct documentation](https://open.shopee.com/documents/v2/v2.global_product.get_category?module=90&type=1)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON responses saved to files, with stdout JSON for small responses and concise text summaries for large responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a LinkFox API key and an authorized Shopee merchant or shop; full responses are persisted under a local linkfox session data directory.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
