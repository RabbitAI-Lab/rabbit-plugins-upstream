## Description:

Jiimore-商品发现 helps agents discover Amazon product opportunities from Jiimore data using keyword-driven filters for conversion, click growth, profitability, reviews, pricing, seller origin, and listing age.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, Amazon sellers, and commerce analysts use this skill to query Jiimore product-discovery data for keyword-based product mining, emerging-opportunity screening, competitor benchmarking, and FBA profitability filtering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox network services and consumes paid credits for product-discovery queries.

Mitigation: Confirm the user intends to spend credits before repeated calls, pagination, retries with changed parameters, or billing actions.

Risk: Authentication and onboarding flows may handle phone numbers, SMS codes, API keys, and payment-order creation.

Mitigation: Use these flows only when the user explicitly requests account or billing setup, and treat generated or displayed API keys as secrets.

Risk: The skill stores full product-discovery responses locally, which can include complete result data beyond the visible summary.

Mitigation: Run it only in an appropriate workspace, review saved files before sharing, and prefer selective extraction from saved JSON over exposing full responses.

Risk: Automatic feedback reporting can send skill-use feedback to LinkFox services.

Mitigation: Keep feedback factual, avoid including unnecessary user-sensitive details, and review whether feedback submission is appropriate for the task.

## Reference(s):

- [Jiimore Product Discovery API Reference](artifact/references/api.md)
- [Authentication and Credits Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-jiimore-product-discovery)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON product-discovery results printed to stdout or saved as local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries require a keyword, support US, JP, and DE marketplaces, cap page size at 100, and use decimal values for rate filters.]

## Skill Version(s):

1.0.6 (source: evidence.release.version; target metadata agrees)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
