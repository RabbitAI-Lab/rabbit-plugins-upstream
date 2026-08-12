## Description:

Queries LinkFox MPSTATS data for Ozon Russia products under a specified brand and returns per-SKU sales, revenue, price, rating, stock, turnover, and lost-sales metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace analysts, e-commerce operators, and developers use this skill to inspect the SKU mix and performance of a single Ozon brand for competitor audits, brand structure analysis, and bestseller review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill handles account signup, API-key generation, and payment ordering in addition to analytics.

Mitigation: Review the authentication and billing flow before installation, obtain and store the LinkFox API key yourself where possible, and confirm any paid plan or QR payment before proceeding.

Risk: The security guidance warns against running the skill with overridden LinkFox endpoint environment variables unless those endpoints are intentionally trusted.

Mitigation: Use the default LinkFox endpoints unless a trusted administrator has approved the override values.

Risk: The skill writes API responses and generated LinkFox data to local session directories.

Mitigation: Keep generated LinkFox data out of repositories and review saved JSON before sharing it outside the workspace.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-mpstats-ozon-brand-products)
- [MPSTATS Ozon Brand Products API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [JSON, Files, Markdown, Shell commands, Guidance]

**Output Format:** [JSON files and stdout JSON or Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a local linkfox session directory; large responses print a compact summary unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
