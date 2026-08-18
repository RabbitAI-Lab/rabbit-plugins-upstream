## Description:

Helps agents work with authorized Shopee store orders through the LinkFox Shopee order API wrappers, including order lookup, package lookup, cancellation, buyer-cancellation handling, notes, booking, invoice, FBS invoice, and prescription-check workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee sellers, operators, and commerce support agents use this skill to query and manage orders for stores already authorized through the companion LinkFox Shopee auth skill. It is suited for order review, package and shipment checks, cancellation decisions, notes, invoice workflows, and related operational follow-up.

### Deployment Geography for Use:

Global, subject to Shopee regional API availability for invoice, FBS invoice, buyer-invoice, and prescription-check operations.

## Known Risks and Mitigations:

Risk: The skill can perform live Shopee order operations, including cancellation, split or unsplit, note updates, buyer-cancellation handling, invoice actions, payment-related onboarding, and prescription checks.

Mitigation: Require explicit confirmation of the shop, order or package identifier, and intended effect before any state-changing or payment-related action.

Risk: The skill depends on LinkFox gateway access and may handle API keys, store identifiers, order data, customer information, invoice details, shipment data, and business records.

Mitigation: Install only when the user trusts LinkFox's gateway, configure API keys directly where possible, and avoid sharing phone numbers or SMS codes with the agent unless the user chooses the onboarding flow.

Risk: Full API responses may be saved locally and could contain sensitive order, customer, invoice, shipment, or business data.

Mitigation: Treat saved response files as sensitive operational data, review local retention expectations, and avoid exposing full response files unless needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-orders)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [Shopee Open Platform Order module](https://open.shopee.com/documents/v2/v2.order.get_order_list?module=94&type=1)
- [Order API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls, JSON, files]

**Output Format:** [Markdown guidance with shell commands and JSON API responses; large responses are summarized while full JSON is saved locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a LinkFox API key and an authorized Shopee store; full API responses may be written under a local linkfox session data directory.]

## Skill Version(s):

1.0.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
