## Description:

Seerfar-Ozon市场关键词搜索 helps agents search Seerfar's Ozon and Wildberries keyword dataset by volume, growth, seller and product counts, price, sales, conversion concentration, and related market metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators, e-commerce analysts, and agent developers use this skill to find and rank Ozon and available Wildberries search terms by demand, competition, price, sales, and conversion metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox account login, API-key issuance, and billing actions.

Mitigation: Require explicit user confirmation before phone login, token generation, plan selection, recharge, or payment-order creation.

Risk: The skill sends marketplace keyword queries and credentials to LinkFox services.

Mitigation: Install and use it only when the user trusts LinkFox with Ozon/Wildberries market queries, account data, and API keys.

Risk: The skill saves full API responses, cache entries, session metadata, and payment QR files locally.

Mitigation: Treat saved outputs as sensitive and delete response, cache, session, and QR files when they are no longer needed.

Risk: The security verdict is suspicious because the package combines keyword research with payment, credential, feedback, and persistent-storage behavior.

Mitigation: Review the skill before deployment and avoid unattended execution of onboarding, billing, or feedback-related commands.

## Reference(s):

- [Seerfar Ozon Market Keyword Search API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-market-keyword-search)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown summaries and tables, shell commands, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The script writes full API responses to a local linkfox session data directory and may print summaries for large responses.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
