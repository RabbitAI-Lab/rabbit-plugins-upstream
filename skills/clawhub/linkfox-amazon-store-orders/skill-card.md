## Description:

Enables agents to search, inspect, and update Amazon SP-API Orders through LinkFox's developer proxy, including order details, buyer and address data, order items, shipment status, regulated order information, verification status, and shipment confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and store operators can use this skill through an agent to retrieve order lists and details, inspect buyer, address, item, and regulated-order data, and perform shipment or verification updates after confirming the action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Amazon order data, buyer and address information, and other sensitive account data.

Mitigation: Install only when LinkFox is trusted for this data, avoid routing credentials to custom hosts, and protect or delete saved response files after use.

Risk: The skill includes order-state-changing workflows such as shipment confirmation, shipment status updates, and regulated-order verification updates.

Mitigation: Manually review the target order, request body, and intended business outcome before allowing an agent to run a state-changing command.

Risk: Authentication, billing, and payment onboarding flows are bundled with the skill and may affect account access or spending.

Mitigation: Confirm any account, billing, payment, or recharge action with the user before proceeding.

## Reference(s):

- [LinkFox Amazon Orders API and Gateway Usage](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-orders)
- [Amazon SP-API searchOrders](https://developer-docs.amazon.com/sp-api/reference/searchorders)
- [Amazon SP-API getOrder](https://developer-docs.amazon.com/sp-api/reference/getorder-3)
- [Amazon SP-API getOrderItems](https://developer-docs.amazon.com/sp-api/reference/getorderitems)
- [Amazon SP-API updateShipmentStatus](https://developer-docs.amazon.com/sp-api/reference/updateshipmentstatus)
- [Amazon SP-API confirmShipment](https://developer-docs.amazon.com/sp-api/reference/confirmshipment)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [JSON files and stdout JSON or summaries, with Markdown guidance for setup and troubleshooting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full responses under ./linkfox/<date>/<session>/data unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
