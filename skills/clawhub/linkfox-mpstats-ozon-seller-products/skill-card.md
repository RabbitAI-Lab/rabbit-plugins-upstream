## Description:

Queries MPSTATS Ozon Russia seller-product data by numeric seller ID and returns per-SKU sales, revenue, pricing, ratings, inventory, turnover, lost sales, filtering, sorting, and currency-conversion views.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce analysts, marketplace operators, and developers use this skill to audit an Ozon seller's SKU portfolio, identify top products, inspect stockout and turnover signals, and compare competitor stores using seller-scoped product metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys and can guide phone/SMS onboarding.

Mitigation: Prefer self-service API-key setup through LinkFox, avoid sharing phone or SMS data unless onboarding is explicitly required, and restart the agent session after configuring the key.

Risk: Endpoint environment variables can change where LinkFox requests are sent.

Mitigation: Before running the skill, verify LINKFOX_* endpoint variables point to official LinkFox domains or leave them unset to use the documented defaults.

Risk: The billing and order flow can create payment actions.

Mitigation: Use billing commands only after the user explicitly requests a purchase path, and validate the plan and payment method before placing an order.

Risk: Full API responses are saved locally and may include detailed seller-query results.

Mitigation: Treat generated linkfox session files as local data artifacts, review their contents before sharing, and remove them when no longer needed.

Risk: Seller-product queries consume LinkFox credits and repeated calls can increase cost.

Mitigation: Confirm credit cost before execution, rely on the 24-hour cache for repeated identical requests, and avoid automatic retries with modified parameters.

## Reference(s):

- [MPSTATS Ozon seller-products API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-mpstats-ozon-seller-products)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown summaries and JSON API responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The script writes the full API response to a local linkfox session data file and prints either the full JSON or a compact summary depending on response size.]

## Skill Version(s):

1.0.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
