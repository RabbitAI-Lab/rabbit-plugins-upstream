## Description:

Filters a historical LinkFox Amazon opportunity metrics pool to find US niche and keyword candidates by market size, growth, competition, pricing, demographics, product features, and review themes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce researchers use this skill to translate business criteria such as low competition, fast growth, pricing gaps, demographics, or review pain points into candidate US Amazon niches and keywords. The skill is for reverse discovery from historical niche-level metrics, not real-time ASIN-level product research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys, SMS login, account tokens, payment-order creation, and Amazon research queries.

Mitigation: Use it only when the publisher is trusted, prefer managed or session-scoped secret storage, and avoid exposing API keys or account tokens in shared shell history, logs, or project files.

Risk: Endpoint environment variables can redirect LinkFox API traffic.

Mitigation: Keep default LinkFox endpoints unless there is a reviewed operational reason to override them, and inspect environment overrides before running the scripts.

Risk: Feedback reporting may include private user intent or business context if copied directly from a session.

Mitigation: Review feedback content before submission and remove confidential customer, product, keyword, or strategy details.

Risk: Successful searches and onboarding flows can consume credits or create payment orders.

Mitigation: Get explicit user confirmation before paid calls or order creation, avoid automatic repeated queries, and use the built-in cache for repeated identical searches.

Risk: The screener writes full API responses and cache files under the current working directory.

Mitigation: Run it from an appropriate workspace, review saved files before sharing the project, and remove stored response data when it is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-opportunity-search-by-metrics)
- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance, JSON API parameters, shell commands, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries must include at least one keyword, niche name, or metric filter; results are US-only, niche-level snapshots and may be cached or written under the working directory.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
