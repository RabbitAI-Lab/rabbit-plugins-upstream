## Description:

Queries and filters independent Shopify stores by dimensions such as name or domain, country, store age, product count, ad count, monthly visits, monthly orders, and social followers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to discover Shopify stores and compare storefront signals for prospecting, competitive research, or market analysis. It also provides guidance for LinkFox credential setup and billing remediation when access or balance issues block a query.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a LinkFox API key and can persist query results in local LinkFox session or cache files.

Mitigation: Install only when the user is comfortable granting that access, and periodically delete local LinkFox cache or session files when query results are sensitive.

Risk: Troubleshooting can involve SMS login, API key generation, and paid plan ordering.

Mitigation: Prefer the self-service LinkFox account page for credentials, do not share OTPs unless the user intends to authenticate, and review any plan purchase before confirming it.

Risk: Queries consume credits dynamically based on the number of stores returned, so broad searches or additional pages can create higher-than-expected cost.

Mitigation: Warn the user before large or repeated queries, keep page size scoped to the task, and ask for confirmation before continuing when a query may consume many credits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopify-store-query)
- [Shopify 店铺查询 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [LinkFox account page](https://agent.linkfox.com/)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON query responses, summaries, and file paths to saved result data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full Shopify query responses are saved to LinkFox session data files; larger responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
