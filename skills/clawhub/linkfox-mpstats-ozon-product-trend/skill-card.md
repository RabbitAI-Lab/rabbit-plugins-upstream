## Description:

This skill helps an agent retrieve daily MPSTATS time-series data for one Ozon Russia SKU, including price, sales, stock, rating, comments, and optional search-visibility signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators, analysts, and agent users use this skill to inspect the day-by-day trend for a single Ozon product SKU and distinguish growth, seasonality, stockouts, missing observations, and price changes. It supports analysis and reporting, not purchasing or investment advice.

### Deployment Geography for Use:

Global; the covered marketplace data is specific to Ozon Russia.

## Known Risks and Mitigations:

Risk: The security evidence reports account onboarding, phone/SMS verification, API-key handling, credit purchases, and local saved outputs.

Mitigation: Install only if the user trusts LinkFox for these flows; prefer the LinkFox self-service website for login and billing, and avoid storing long-lived API keys in shell startup files on shared or managed machines.

Risk: The security evidence reports broad credential-bearing network behavior and warns about gateway URL overrides.

Mitigation: Review configured LinkFox environment variables before use, avoid overriding gateway URLs unless the endpoint is trusted, and keep API keys scoped to appropriate accounts.

Risk: The artifact includes billing flows for listing plans, creating orders, and rendering payment QR codes.

Mitigation: Require explicit user consent before any paid action, verify the plan and payment method, and use official LinkFox billing channels where possible.

Risk: The artifact describes automatic feedback submission when behavior, results, or user sentiment indicate feedback is appropriate.

Mitigation: Review whether feedback submission is acceptable in the deployment context before enabling or using this behavior.

## Reference(s):

- [MPSTATS Ozon Product Trend API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Listing](https://clawhub.ai/linkfox-ai/skills/linkfox-mpstats-ozon-product-trend)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown/table summaries, shell command guidance, and saved JSON API responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The tool writes full API responses under a local linkfox session data directory, prints small responses inline, summarizes larger responses, and uses a 24-hour local cache for repeated parameter sets.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
