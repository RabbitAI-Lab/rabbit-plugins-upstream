## Description:

This skill helps agents query Shopee Account Health data through LinkFox, including shop performance, metric source details, penalty points, punishment history, listing issues, and late orders for authorized stores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and operators supporting Shopee stores use this skill to inspect store health, identify poor-performing metrics, review penalties and punishments, and locate late orders or listings that need action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Shopee account-health requests and API-key-authenticated calls through LinkFox services.

Mitigation: Use it only when the user accepts LinkFox handling Shopee account-health data and API keys; prefer self-service key setup at the provider site.

Risk: The onboarding flow can include phone-based login and paid-plan checkout with QR-code payment.

Mitigation: Confirm the selected plan, payment method, and order details before scanning or sharing any payment QR code.

Risk: Full response payloads and QR files may be saved locally without redaction.

Mitigation: Delete saved linkfox response data and QR files when they are no longer needed, and avoid using --inline unless full output is necessary.

Risk: Endpoint override environment variables can redirect calls away from the default LinkFox services.

Mitigation: Do not set or override LinkFox endpoint environment variables unless the target service is explicitly trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-account-health)
- [Account Health API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [Shopee get_shop_performance documentation](https://open.shopee.com/documents/v2/v2.account_health.get_shop_performance?module=103&type=1)
- [Shopee get_metric_source_detail documentation](https://open.shopee.com/documents/v2/v2.account_health.get_metric_source_detail?module=103&type=1)
- [Shopee get_penalty_point_history documentation](https://open.shopee.com/documents/v2/v2.account_health.get_penalty_point_history?module=103&type=1)
- [Shopee get_punishment_history documentation](https://open.shopee.com/documents/v2/v2.account_health.get_punishment_history?module=103&type=1)
- [Shopee get_listings_with_issues documentation](https://open.shopee.com/documents/v2/v2.account_health.get_listings_with_issues?module=103&type=1)
- [Shopee get_late_orders documentation](https://open.shopee.com/documents/v2/v2.account_health.get_late_orders?module=103&type=1)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [JSON files and console text summaries, with optional full inline JSON output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are saved under a local linkfox session data directory; responses of 8 KB or less print in full, larger responses print summaries unless --inline is used.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
