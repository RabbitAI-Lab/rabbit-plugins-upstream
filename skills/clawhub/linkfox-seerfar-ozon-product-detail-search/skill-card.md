## Description:

Fetches detailed Seerfar analytics for a single Ozon SKU, including product identity, pricing, reviews, sales and revenue estimates, stock, category rank, seller, brand, fulfillment, and listing age.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, analysts, and agent users use this skill to inspect one Ozon product by SKU for product-detail reporting, competitor teardown, listing diagnostics, and sales-trend tracking. It is not intended for product discovery, shop catalog browsing, keyword mining, or batch comparison without one call per SKU.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on LinkFox account credentials and may guide users through login, API key setup, and billing flows.

Mitigation: Use the first-party LinkFox site for login or billing when possible, run onboarding or order commands only intentionally, and treat API keys, SMS codes, payment orders, and payment QR outputs as sensitive.

Risk: Full API responses and cached results may be written to generated linkfox directories in the user's workspace.

Mitigation: Review saved response files before sharing a workspace and delete generated linkfox data that is no longer needed.

Risk: Each product-detail lookup consumes LinkFox credits, and repeated SKU comparisons can incur additional cost.

Mitigation: Confirm the SKU and date range before execution, rely on the 24-hour cache for repeated identical calls, and ask before running additional paid lookups.

Risk: Sales and revenue values are Seerfar estimates, not official Ozon figures.

Mitigation: Present metrics as analytics estimates, include the selected date range, and avoid using the output as the sole source for financial or operational decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-product-detail-search)
- [Seerfar Ozon Product Detail API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration guidance]

**Output Format:** [JSON responses saved to local files, with concise text or Markdown summaries and shell-command guidance for authentication and billing setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an Ozon SKU, supports an optional dateRange, uses a LinkFox API key, caches repeated calls for 24 hours, and may persist full API responses under a generated linkfox session directory.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
