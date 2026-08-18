## Description:

FastMoss-TikTok商品搜索 helps agents search and filter TikTok Shop product data across supported markets using keyword, category, shop type, sales, GMV, commission, creator-count, and sorting filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and e-commerce analysts use this skill to retrieve TikTok Shop product-search results from FastMoss and compare product performance signals such as sales, GMV, commission rate, rating, shop type, and creator promotion counts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid LinkFox/FastMoss integration and each product search can consume credits.

Mitigation: Confirm expected credit cost with the user before repeated searches, pagination, or retries that could create additional charges.

Risk: Authentication and onboarding flows may ask for a phone number, handle SMS login, generate an API key, and create payment orders.

Mitigation: Use the onboarding flow only after explicit user consent, verify the selected plan and payment method, and do not poll payment status unless the user asks.

Risk: API keys may be printed or stored in persistent environment configuration.

Mitigation: Avoid persistent plaintext API-key storage on shared or managed machines and rotate credentials if they are exposed in logs or terminal history.

Risk: Full product-search API responses are stored locally and may contain commercial research data.

Mitigation: Review the local linkfox session output directory, avoid committing saved responses, and delete stored responses when they are no longer needed.

Risk: The skill can send feedback to LinkFox when it detects praise, dissatisfaction, mismatch, or improvement opportunities.

Mitigation: Keep feedback concise, avoid sensitive user or business data, and disclose feedback submission when it is material to the user's workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-fastmoss-product-search)
- [FastMoss-TikTok商品搜索 API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries, JSON product-search responses, and setup or billing commands when authentication or credits are required.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may save full API responses under a local linkfox session directory and print a summary for large responses.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
