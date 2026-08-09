## Description:

LinkFox's Lingxing ERP skill helps agents use the Lingxing OpenAPI for Amazon advertising, orders, listings, inventory, finance, FBA, purchasing, customer service, and multi-platform commerce workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query Lingxing ERP business data and generate the shell commands, parameters, and configuration needed for Lingxing OpenAPI calls. It is most relevant when an agent needs to inspect Amazon store, advertising, order, listing, inventory, finance, FBA, purchasing, customer service, or multi-platform commerce data through the bundled CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundle includes LinkFox account, SMS login, billing, and payment flows in addition to the stated Lingxing ERP wrapper.

Mitigation: Install only when those helper flows are intentionally desired, and do not enter phone codes or create payment orders unless the LinkFox flow is trusted.

Risk: Lingxing credentials and ERP responses may expose commercial data or PII.

Mitigation: Use least-privilege Lingxing AppID/AppSecret permissions and clean up saved response files after use.

Risk: Some supported Lingxing endpoints may write or alter ERP data.

Mitigation: Prefer read-only endpoints and avoid write endpoints unless the user explicitly intends the action.

Risk: Overridden LINKFOX_* endpoint environment variables could redirect account helper traffic.

Mitigation: Keep LinkFox endpoint environment variables unset or verify them before using onboarding, billing, or payment commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-lingxing-erp)
- [Lingxing OpenAPI host](https://openapi.lingxing.com)
- [API usage guide](artifact/references/api.md)
- [Onboarding and account helper guide](artifact/references/onboarding.md)
- [Sales API reference](artifact/references/sale-full.md)
- [Finance API reference](artifact/references/finance.md)
- [Warehouse API reference](artifact/references/warehouse.md)
- [Statistics API reference](artifact/references/statistics.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Lingxing AppID/AppSecret credentials and may persist large API responses to local files when the response helper is used.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
