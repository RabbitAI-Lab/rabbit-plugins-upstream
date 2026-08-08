## Description:

Finds Amazon products competing in the same Jiimore niche as a reference ASIN and supports filtering by conversion, clicks, sales, reviews, ratings, price, FBA fees, and gross margin.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce analysts use this skill to find same-niche competitors for a reference ASIN and compare marketplace metrics. It is suited to objective competitor discovery and filtering, not keyword research, ad management, supplier sourcing, or listing optimization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ASIN queries, session metadata, and LinkFox responses are sent to LinkFox services and full responses may be stored locally.

Mitigation: Use the skill only when this data sharing and local storage are acceptable, and periodically delete local LinkFox response and cache files if the data is sensitive.

Risk: The skill may involve phone/SMS login, API-key handling, and payment or billing flows.

Mitigation: Prefer obtaining API keys and completing payments directly on the LinkFox website, and avoid sharing more credential or payment data through the agent than needed.

Risk: Custom LinkFox endpoint environment variables can redirect requests away from default LinkFox services.

Mitigation: Avoid setting custom LinkFox endpoint environment variables unless the destination is fully trusted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-jiimore-page-asins-by-asin)
- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses, local JSON data files, and shell commands for API and onboarding flows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses under the LinkFox session data directory, caches identical queries for 24 hours, and summarizes responses larger than 8 KB unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
