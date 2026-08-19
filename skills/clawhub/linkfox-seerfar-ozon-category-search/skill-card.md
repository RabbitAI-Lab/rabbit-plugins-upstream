## Description:

Searches a Seerfar Ozon category by category ID and returns category aggregates plus product-level sales, price, rating, review, brand, seller, and fulfillment metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace analysts, and developers use this skill to inspect one Ozon category, size demand, compare price bands, and rank products by sales, revenue, price, or rating.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires network access and a LinkFox API key to query the Seerfar Ozon category endpoint.

Mitigation: Install only in environments where LinkFox API access is intended, and scope or rotate the API key according to organizational policy.

Risk: Full API responses are stored locally and may contain marketplace analysis data from the user's queries.

Mitigation: Review the LinkFox session data directory retention policy and remove saved response files when they are no longer needed.

Risk: The bundled onboarding flow can involve phone numbers, SMS codes, account setup, billing plans, and payment actions.

Mitigation: Use onboarding or recharge commands only after explicit user consent, and verify payment details before submitting an order.

Risk: Endpoint environment variables can redirect the skill to alternate LinkFox-compatible services.

Mitigation: Review and restrict LinkFox endpoint environment variables before use in managed or production workspaces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-category-search)
- [Seerfar Ozon category search API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries and tables with saved JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a LinkFox API key; full API responses are saved locally in the LinkFox session data directory, with large responses summarized on stdout.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
