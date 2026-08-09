## Description:

亚马逊店铺订单 skill uses LinkFox's developer proxy to call Amazon SP-API Orders operations for order search, order details, buyer information, shipping addresses, order items, regulated order data, verification status updates, shipment status updates, and shipment confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and Amazon sellers use this skill to retrieve and update Amazon store order data through LinkFox's gateway-backed SP-API Orders scripts. It supports operational order lookup, buyer and address retrieval, order-item inspection, regulated-order status handling, and shipment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Amazon order data, API keys, phone/SMS login flows, and payment-plan actions through LinkFox-controlled services.

Mitigation: Use the skill only when the user trusts LinkFox for these workflows, and confirm account, billing, and payment actions before running onboarding commands.

Risk: Full order responses are saved to local linkfox session data files, which may contain sensitive Amazon order or buyer information.

Mitigation: Run the skill in a workspace where saved response files are excluded from commits and sharing, and redact sensitive values before attaching logs or feedback.

Risk: Endpoint override environment variables can redirect gateway traffic and expose credentials or order data to an unintended destination.

Mitigation: Avoid LINKFOX_TOOL_GATEWAY, STORE_API_BASE_URL, SPAPI_BASE_URL, and related onboarding endpoint overrides unless the destination is explicitly controlled and trusted.

Risk: Some Orders operations can access restricted buyer, address, or regulated-order data.

Mitigation: Use only the minimum required Orders operation and includedData fields, and follow Amazon restricted-data requirements when buyer, address, or regulated-order information is requested.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-orders)
- [API and gateway usage reference](artifact/references/api.md)
- [Authentication and billing onboarding reference](artifact/references/onboarding.md)
- [Amazon SP-API searchOrders](https://developer-docs.amazon.com/sp-api/reference/searchorders)
- [Amazon SP-API getOrder](https://developer-docs.amazon.com/sp-api/reference/getorder-3)
- [Amazon SP-API confirmShipment](https://developer-docs.amazon.com/sp-api/reference/confirmshipment)
- [Amazon SP-API Restricted Data Token](https://developer-docs.amazon.com/sp-api/reference/createrestricteddatatoken)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON files]

**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts print full JSON for responses up to 8 KB, otherwise print summaries unless --inline is used; full responses are always saved under a linkfox session data directory.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
