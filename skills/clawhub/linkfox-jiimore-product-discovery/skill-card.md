## Description:

Jiimore Product Discovery helps Amazon sellers find high-potential products by querying Jiimore data with keyword, marketplace, conversion, click-growth, margin, review, and listing-age filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and e-commerce operators use this skill to run keyword-based product discovery for US, Japan, and Germany marketplaces and review factual product candidates by conversion, click growth, profitability, reviews, and launch date.

### Deployment Geography for Use:

Global, with product discovery data limited to Amazon US, Japan, and Germany marketplaces.

## Known Risks and Mitigations:

Risk: The skill can consume paid LinkFox/Jiimore credits through product-discovery queries.

Mitigation: Confirm with the user before any credit-consuming query, state the 9-credit cost when relevant, and avoid repeated automatic retries with altered parameters.

Risk: The skill handles LinkFox account login, API keys, and payment/order flows.

Mitigation: Prefer the self-service API-key flow, keep API keys out of shared logs, and require explicit user confirmation before SMS login, API-key generation, or payment/order commands.

Risk: The skill writes LinkFox response data to local files.

Mitigation: Tell users where response files are written when data is saved and avoid exposing saved API responses or credentials in shared contexts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-jiimore-product-discovery)
- [Jiimore Product Discovery API Reference](references/api.md)
- [Authentication and Credits Onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown product summaries, JSON API responses, and setup commands or configuration guidance when authentication or billing action is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries require a keyword; result sets may be cached for 24 hours and full responses are written to a local linkfox data directory.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
