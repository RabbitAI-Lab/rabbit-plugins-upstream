## Description:

Batch-fetches MPSTATS Ozon Russia product-card data for up to 100 SKU IDs, including price, discounts, Ozon Card price, rating, reviews, stock, sales, revenue, listing date, and images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators, analysts, and developers use this skill to retrieve per-SKU Ozon product-card metrics for competitor checks, stock and price audits, and period-level sales comparisons. It is intended for users who already have Ozon SKU IDs or have obtained them from another search or drill-down workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill calls LinkFox/MPSTATS services using an API key and can send SKU queries and session headers to those services.

Mitigation: Use a dedicated LinkFox API key, avoid sharing secrets in prompts or logs, and only run the skill when sending Ozon SKU data to LinkFox/MPSTATS is acceptable.

Risk: Full product-detail responses are saved and cached locally, which can persist marketplace analysis data beyond the visible chat output.

Mitigation: Review and clean the generated linkfox session data and cache directories when the results contain sensitive competitive or commercial analysis.

Risk: The bundled onboarding helper can list paid plans and create payment orders.

Mitigation: Prefer self-service API-key setup, require explicit user confirmation before creating any payment order, and do not actively poll payment status unless the user asks.

Risk: Custom LINKFOX_* base URL environment variables can redirect API, login, or billing traffic.

Mitigation: Keep default endpoints unless the destination is trusted and intentionally configured.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-mpstats-ozon-product-detail)
- [MPSTATS Ozon product-detail API reference](references/api.md)
- [Authentication and billing onboarding guide](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON responses saved to local files with stdout JSON or summary text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses under a linkfox session data directory; uses a 24-hour local cache; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
