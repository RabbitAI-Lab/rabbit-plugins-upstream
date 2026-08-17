## Description:

Retrieves product lists and shop-level 30-day sales metrics for a specified Ozon seller or shop ID from Seerfar to support competitor shop analysis and bestseller discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and e-commerce analysts use this skill to inspect one Ozon shop's catalog by seller ID, including item prices, ratings, fulfillment model, seller type, return/cancellation rate, and 30-day sales. It is intended for competitor-shop product analysis, bestseller mining, and seller catalog review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports sensitive account, API-key, billing, feedback, and local-retention behavior.

Mitigation: Use the skill only in a trusted workspace, review onboarding and feedback behavior before use, and avoid sharing API keys, phone numbers, SMS codes, or payment actions without explicit user consent.

Risk: Endpoint override environment variables can redirect outbound requests.

Mitigation: Set endpoint override variables only when the destination is controlled and expected; otherwise rely on the documented default LinkFox endpoints.

Risk: Full search results are saved locally and may include commercially sensitive shop analysis data.

Mitigation: Treat saved JSON files as retained user data, store them in an appropriate workspace, and delete them when they are no longer needed.

Risk: The skill consumes paid credits and may trigger billing flows during quota resolution.

Mitigation: Warn users before repeated calls or pagination and require explicit approval before starting recharge or paid-order steps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-shop-search)
- [Seerfar Ozon shop search API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON files, Shell commands, Configuration guidance]

**Output Format:** [Markdown tables and summaries with saved JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The search script caches identical requests for 24 hours, saves full responses under a linkfox session directory, and summarizes large responses unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
