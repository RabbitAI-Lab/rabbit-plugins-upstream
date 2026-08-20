## Description:

Queries Shopee Account Health data through LinkFox for authorized stores, including shop performance, metric source details, penalty points, punishment history, listings with issues, and late orders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee sellers and their agents use this skill to inspect authorized store health metrics, investigate penalties and listing issues, review late orders, and decide operational follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive Shopee store health, penalty, listing, order, and account-health data through LinkFox services.

Mitigation: Install only when the user trusts LinkFox with this store data and understands that API calls are routed through LinkFox endpoints.

Risk: The bundled onboarding flow can involve phone/SMS login, API-key generation, billing, and payment-order handling.

Mitigation: Prefer configuring a pre-existing API key manually, and use the phone/SMS or payment commands only when they are necessary and expected.

Risk: Endpoint environment variables can redirect API traffic away from the expected LinkFox services.

Mitigation: Verify LinkFox endpoint environment variables point to LinkFox domains before using the skill with store or payment data.

Risk: Local LinkFox session files may persist sensitive store or payment-related data.

Mitigation: Review and clean up local LinkFox session data after use, especially in shared or long-lived workspaces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-account-health)
- [Shopee Account Health get_shop_performance](https://open.shopee.com/documents/v2/v2.account_health.get_shop_performance?module=103&type=1)
- [Shopee Account Health get_late_orders](https://open.shopee.com/documents/v2/v2.account_health.get_late_orders?module=103&type=1)
- [Shopee Account Health get_listings_with_issues](https://open.shopee.com/documents/v2/v2.account_health.get_listings_with_issues?module=103&type=1)
- [Shopee Account Health get_metric_source_detail](https://open.shopee.com/documents/v2/v2.account_health.get_metric_source_detail?module=103&type=1)
- [Shopee Account Health get_penalty_point_history](https://open.shopee.com/documents/v2/v2.account_health.get_penalty_point_history?module=103&type=1)
- [Shopee Account Health get_punishment_history](https://open.shopee.com/documents/v2/v2.account_health.get_punishment_history?module=103&type=1)
- [Account Health API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON responses, saved JSON files, summaries, and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are written to LinkFox session data; stdout prints complete JSON for responses up to 8 KB or summaries unless --inline is used.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
