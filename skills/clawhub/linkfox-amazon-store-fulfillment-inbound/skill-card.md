## Description:

Helps agents manage Amazon FBA Fulfillment Inbound workflows through LinkFox, including inbound plans, packing, placement, shipments, delivery windows, self-ship appointments, transportation options, prep, compliance, labels, and bill of lading retrieval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and their agents use this skill to run Amazon Fulfillment Inbound and FBA receiving workflows for authorized stores. It is intended for creating and recovering inbound plans, evaluating packing, placement, transportation, and delivery choices, and retrieving labels or shipment documents after explicit user review where required.

### Deployment Geography for Use:

Global, subject to Amazon marketplace and Fulfillment Inbound regional restrictions.

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys, login tokens, billing flows, and Amazon store operations.

Mitigation: Install only when LinkFox is trusted for the target Amazon store and account billing flow, and treat LINKFOX_AGENT_API_KEY as a secret.

Risk: Endpoint override variables can redirect traffic away from the default LinkFox gateway.

Mitigation: Use the default LinkFox endpoints and avoid LINKFOX_TOOL_GATEWAY or related endpoint overrides unless the target endpoint is fully controlled.

Risk: Full Amazon operation responses are persisted locally under linkfox session folders.

Mitigation: Review local response files for sensitive business data and manage retention according to the user's data handling requirements.

Risk: Some operations can affect shipment choices, transportation charges, appointments, or account billing.

Mitigation: Review plans, prices, store identity, and operation targets before running write, order, payment, or transportation confirmation commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-fulfillment-inbound)
- [Fulfillment Inbound API reference](references/api.md)
- [Fulfillment Inbound workflows](references/workflows.md)
- [ID and cross-version rules](references/identifiers.md)
- [Marketplace constraints](references/marketplace-constraints.md)
- [Authentication, authorization, and billing onboarding](references/onboarding.md)
- [Amazon Fulfillment Inbound API overview](https://developer-docs.amazon.com/sp-api/docs/fulfillment-inbound-api)
- [Amazon Fulfillment Inbound v2024-03-20 reference](https://developer-docs.amazon.com/sp-api/reference/fulfillment-inbound-v2024-03-20)
- [Amazon Fulfillment Inbound v2024-03-20 OpenAPI model](https://github.com/amzn/selling-partner-api-models/blob/main/models/fulfillment-inbound-api-model/fulfillmentInbound_2024-03-20.json)
- [Amazon Fulfillment Inbound v0 OpenAPI model](https://github.com/amzn/selling-partner-api-models/blob/main/models/fulfillment-inbound-api-model/fulfillmentInboundV0.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls, JSON, files]

**Output Format:** [Markdown guidance with shell command examples, JSON parameters, API responses, summaries, and local response files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operation scripts save full successful responses under linkfox session folders and may print either full JSON or a summary depending on response size.]

## Skill Version(s):

1.0.0 (source: server release metadata, released 2026-08-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
