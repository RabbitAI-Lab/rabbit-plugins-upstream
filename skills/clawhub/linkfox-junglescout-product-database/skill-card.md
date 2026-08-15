## Description:

Queries Jungle Scout product-database data through LinkFox so agents can filter Amazon products across 10 marketplaces by category, price, sales, revenue, reviews, rating, BSR rank, LQS, seller type, and related criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and agents use this skill to discover and compare Amazon products by commercial filters such as monthly sales, revenue, price, reviews, BSR rank, listing quality, and fulfillment type. It also guides users through LinkFox authentication or billing recovery when required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid Jungle Scout queries and dynamic token charges may consume credits unexpectedly.

Mitigation: Warn users before additional paid calls, avoid automatic retry or broadening searches after empty results, and use the local cache for repeated identical queries.

Risk: The onboarding flow can process phone-based login, OTP codes, API key issuance, paid-plan ordering, and payment QR generation.

Mitigation: Use onboarding only when the user explicitly chooses it, treat OTPs and API keys as secrets, and avoid exposing payment or account details beyond what the user needs to complete setup.

Risk: Complete API responses are written to local LinkFox session and cache files.

Mitigation: Store outputs only in an appropriate workspace, review saved result files before sharing, and remove cached data when product research results should not persist.

Risk: Automatic feedback reporting can disclose task context or user sentiment to the publisher endpoint.

Mitigation: Keep feedback concise, avoid confidential user or business data, and report only information needed to describe the skill issue or outcome.

## Reference(s):

- [Jungle Scout Product Database API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-junglescout-product-database)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown tables and summaries, inline JSON for small responses, JSON files for complete responses, and shell commands for onboarding or configuration.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The query script caches identical parameters for 24 hours and writes full responses under a LinkFox session data directory; large responses print a compact summary unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
