## Description:

Analyzes Amazon niche market data for a reference ASIN, including competitive intensity, brand concentration, new-product success rate, pricing, demand, and opportunity metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, e-commerce analysts, and agent developers use this skill to query Jiimore/LinkFox data by ASIN and summarize the niche segments that a product competes in. It supports market-scanning tasks such as competition, brand concentration, demand, CPC, pricing, and new-product viability analysis.

### Deployment Geography for Use:

Global; market data queries are limited to US, JP, and DE Amazon marketplaces.

## Known Risks and Mitigations:

Risk: The integration consumes paid LinkFox/Jiimore credits and can guide payment-order creation when credits are insufficient.

Mitigation: Confirm cost expectations before repeated calls and require explicit user approval before any payment or recharge step.

Risk: The scripts read a LinkFox API key from environment variables.

Mitigation: Store API keys only in the intended environment variables, avoid pasting keys into prompts or logs, and rotate keys if exposed.

Risk: Full API responses are saved locally and may contain sensitive market-research details.

Mitigation: Run the skill in the intended workspace, review saved response files before sharing the workspace, and delete session data that should not persist.

Risk: Automatic feedback reporting can send user-described outcomes or business context to LinkFox.

Mitigation: Do not use the feedback flow with sensitive business details unless the user explicitly consents to that disclosure.

## Reference(s):

- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-jiimore-get-niche-info-by-asin)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown tables and summaries, JSON API responses saved to local files, and shell commands for optional authentication or billing flows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill saves full API responses under a linkfox session data directory, uses a 24-hour local cache for identical parameters, prints full stdout for responses up to 8 KB, and summarizes larger responses unless --inline is used.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
