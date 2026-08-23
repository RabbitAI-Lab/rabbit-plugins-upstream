## Description:

Supports Amazon Multi-Channel Fulfillment outbound workflows through LinkFox, including delivery offers, order previews, order create/read/list/update/cancel actions, sandbox status/package updates, and related invoice header lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and developers use this skill to manage Amazon MCF outbound fulfillment through authorized LinkFox-backed store access. It helps quote, preview, create, inspect, update, cancel, and track fulfillment orders while keeping invoice-header discovery separate from outbound order operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authoritative security verdict is suspicious because the release bundles under-disclosed LinkFox account, payment, and API-token tooling.

Mitigation: Install only when LinkFox-backed Amazon MCF access is intended, review bundled onboarding and payment commands before use, and avoid those commands unless the account action is explicit.

Risk: Full Amazon order, shipment, tracking, proof-of-delivery, and invoice responses can be stored locally under linkfox output and cache directories.

Mitigation: Treat local LinkFox output as sensitive operational data, keep the workspace controlled, and clear output/cache directories when they contain order or invoice data.

Risk: The skill depends on LinkFox gateway credentials through LINKFOX_AGENT_API_KEY or LINKFOXAGENT_API_KEY.

Mitigation: Limit access to credential environment variables and do not paste or forward Amazon access or refresh tokens into skill inputs.

## Reference(s):

- [Fulfillment Outbound API](https://developer-docs.amazon.com/sp-api/docs/fulfillment-outbound-api)
- [Fulfillment Outbound v2026-07-04 Reference](https://developer-docs.amazon.com/sp-api/reference/fulfillment-outbound-v2026-07-04)
- [Fulfillment Outbound v2026-07-04 OpenAPI Model](https://github.com/amzn/selling-partner-api-models/blob/main/models/fulfillment-outbound-api-model/fulfillmentOutbound_2026-07-04.json)
- [Fulfillment Outbound Migration Guide](https://developer-docs.amazon.com/sp-api/docs/fulfillment-outbound-migration-guide)
- [API Reference](references/api.md)
- [Workflow Guide](references/workflows.md)
- [Onboarding Guide](references/onboarding.md)
- [Migration Notes](references/migration.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Wrappers write full LinkFox responses to local JSON files and may print either full JSON or a summarized response depending on size and flags.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
