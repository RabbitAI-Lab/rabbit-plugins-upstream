## Description:

Fetches full details for a single Ozon product SKU from Seerfar, including title, price in rubles, rating, reviews, Q&A count, sales and revenue over a selected window, stock, category rank, daily sales trend, brand, seller, fulfillment, weight, and listing age.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce analysts use this skill to retrieve and summarize one Ozon product's SKU-level metrics for product deep dives, competitor teardown, listing diagnostics, stock checks, sales trend review, and category-rank tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox and Seerfar as paid external services and consumes credits for product-detail requests.

Mitigation: Use it only when the user expects paid LinkFox/Seerfar service usage, confirm additional calls before high-frequency or repeated lookups, and review account balance or plan details before ordering credits.

Risk: Authentication and onboarding can involve a LinkFox API key, phone number, SMS code, and generated API credentials.

Mitigation: Keep credentials out of chat transcripts, logs, repositories, and screenshots; provide secrets through environment variables; and restart the agent session after setting the key.

Risk: The included scripts create durable local JSON, cache, metadata, and payment QR files under LinkFox output directories.

Mitigation: Review the generated linkfox directory before sharing or committing workspaces, and exclude response data, cache files, API keys, and QR images from source control.

Risk: Environment variables can override LinkFox service endpoints.

Mitigation: Do not set custom LinkFox endpoint environment variables unless the destination host is trusted and appropriate for the user's data and credentials.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-product-detail-search)
- [Seerfar Ozon product detail API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)
- [LinkFox Agent Console](https://agent.linkfox.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown summaries with JSON API responses and persisted JSON data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The product-detail script writes the full response to a LinkFox session data directory, uses a 24-hour local cache by default, prints small responses inline, and summarizes larger responses unless full inline output is requested.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
