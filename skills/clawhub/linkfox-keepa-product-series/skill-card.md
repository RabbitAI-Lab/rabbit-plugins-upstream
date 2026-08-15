## Description:

Queries Amazon product historical time-series data for a single ASIN, including price, BSR, rating, seller count, and monthly sales trends across supported marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, ecommerce analysts, and agents use this skill to retrieve and summarize Keepa-backed historical product metrics for a specific ASIN. It supports pricing, ranking, fulfillment-price, seller-count, rating, and sales-trend comparisons within the documented marketplace and time-window limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox network services and reads a LinkFox API key from environment variables.

Mitigation: Install only in workspaces where the gateway URLs and environment variables are controlled, and avoid shared or untrusted environments.

Risk: The skill can help create or retrieve LinkFox account credentials during onboarding.

Mitigation: Use the onboarding flow only with trusted account details, review generated API-key handling, and restart sessions after setting credentials.

Risk: The billing flow can initiate paid plan orders when credits are insufficient.

Mitigation: Require explicit user confirmation before listing plans or creating payment orders, and do not automatically poll or repeat paid actions.

Risk: Full API responses and payment QR artifacts may be stored locally.

Mitigation: Run the skill in a private workspace and review or clean the LinkFox output directory when responses or payment artifacts may contain sensitive data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-keepa-product-series)
- [Keepa Amazon price history API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses, local JSON files, and shell commands for API use or onboarding.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved locally under a LinkFox session directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
