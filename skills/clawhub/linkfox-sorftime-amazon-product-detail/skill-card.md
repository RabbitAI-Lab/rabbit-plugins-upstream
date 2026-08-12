## Description:

Helps Amazon sellers query Sorftime product detail and historical trend data by ASIN across 14 marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce analysts use this skill to fetch ASIN-level product details, sales, price, BSR, promotion, and profit/FBA-fee trends for product checks and competitor comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid LinkFox/Sorftime service and may consume credits for ASIN lookups and longer trend ranges.

Mitigation: Confirm the user wants to spend credits before running paid queries, use cached results when appropriate, and avoid repeated exploratory calls after failures or empty results.

Risk: The skill stores complete API responses in local linkfox session files, which may include product, seller, or business-analysis data.

Mitigation: Run it only in workspaces where local response files are acceptable, avoid sharing generated files unintentionally, and remove stored responses when they are no longer needed.

Risk: The skill relies on environment-stored API keys and includes account, phone/SMS onboarding, and payment-order helper flows.

Mitigation: Use onboarding and payment commands only after explicit user initiation, protect API keys as credentials, and prefer existing configured credentials when available.

Risk: The skill can report feedback automatically when it detects mismatch, dissatisfaction, praise, or improvement opportunities.

Mitigation: Review or disable feedback reporting before sharing sensitive prompts, product plans, or proprietary business data.

## Reference(s):

- [Sorftime Product Detail API Reference](references/api.md)
- [Authentication and Billing Onboarding Guide](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-sorftime-amazon-product-detail)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a linkfox session directory; large responses print summaries unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
