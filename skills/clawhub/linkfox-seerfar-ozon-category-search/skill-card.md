## Description:

Looks up products in a specified Ozon category through Seerfar and returns category-level aggregates plus product metrics for category selection, best-seller ranking, price-band analysis, and seasonality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce analysts, marketplace operators, and agent users use this skill to retrieve Ozon category product rows, rankings, and aggregate sales, revenue, price, rating, and fulfillment data. It supports category sizing, category best-seller discovery, historical month snapshots, and fulfillment-filtered analysis when a category ID is available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports sensitive phone login, API-key generation, payment-order, automatic feedback, and persistent storage behavior in addition to the advertised Ozon lookup.

Mitigation: Install only if LinkFox is trusted with category queries and account setup data; obtain and configure API keys directly when possible, avoid relaying OTP codes through the agent unless intentionally using the onboarding flow, and review payment actions before proceeding.

Risk: The skill stores full API responses and cache data locally, which may include queried category data and account-related session artifacts.

Mitigation: Review or delete the local linkfox response, session, and cache directories after use, especially on shared workspaces.

Risk: Each lookup consumes credits and repeated pagination or retries can create unexpected cost.

Mitigation: Confirm additional calls with the user when high-frequency lookups, pagination, historical comparisons, or billing recovery are needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-category-search)
- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)
- [LinkFox Agent Setup](https://agent.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API parameters, tabular summaries, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The runtime script writes full API responses under a linkfox session data directory, prints full JSON for small responses, and summarizes larger responses unless inline output is requested.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
