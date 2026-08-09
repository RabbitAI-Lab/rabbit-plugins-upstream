## Description:

Queries Shopify products with filters for keywords or URLs, price, weekly sales, listing date, Facebook ads, competition, supplier availability, shipping country, pagination, and sorting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search and compare Shopify products for independent-store product research, including sales, revenue, advertising, competition, supplier, and shipping-country signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkFox receives Shopify query parameters and related session metadata.

Mitigation: Use only non-sensitive product research inputs and install only when this third-party data sharing is acceptable.

Risk: The skill can help manage LinkFox account setup, API keys, and paid credit purchases.

Mitigation: Use phone, SMS, API-key, plan, order, and payment helpers only when explicitly requested, and review outputs before following payment or credential steps.

Risk: Full Shopify query responses and cache files may be stored locally.

Mitigation: Delete stored LinkFox response and cache files periodically when product query results are sensitive.

Risk: Endpoint environment variables can redirect LinkFox API traffic.

Mitigation: Verify LinkFox endpoint environment variables before execution and avoid running with untrusted overrides.

## Reference(s):

- [Shopify Product Query API Reference](references/api.md)
- [Authentication and Credit Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopify-product-query)
- [LinkFox Agent Portal](https://agent.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON responses, tabular product data, and optional shell commands for debugging or onboarding.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The query helper writes full LinkFox responses to local JSON files and may print either full JSON or a summarized response depending on response size.]

## Skill Version(s):

1.0.8 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
