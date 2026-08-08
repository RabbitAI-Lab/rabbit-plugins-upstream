## Description:

Queries MPSTATS Ozon category-product data for a full Russian category path, returning SKU-level sales, revenue, price, rating, stock, turnover, lost-sales, ranking, and filtering metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Cross-border e-commerce analysts, category researchers, and marketplace operators use this skill to inspect Ozon Russia products within a known Russian category path, compare SKU performance, and find category opportunities. It is data-only and does not provide business advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a LinkFox API key and can use account, phone/SMS, and billing helper flows.

Mitigation: Use a scoped LinkFox account where possible, prefer self-service setup for credentials and payments, and avoid sharing phone or payment steps with the agent unless the workflow requires it.

Risk: Full marketplace API responses are written locally and may contain commercial product, seller, ranking, and performance data.

Mitigation: Run the skill only in workspaces where saved marketplace data is acceptable, and review or remove saved linkfox session data according to local retention needs.

Risk: Environment variables can override LinkFox endpoint URLs.

Mitigation: Avoid untrusted LINKFOX_* endpoint overrides and review the configured gateway URLs before using the skill with credentials.

Risk: The skill may send feedback to LinkFox automatically when it detects quality issues or user sentiment.

Mitigation: Review the feedback behavior before installation and avoid including sensitive user or business details in feedback content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-mpstats-ozon-category-products)
- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON parameters, shell commands, API response summaries, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under the workspace linkfox session data directory; small responses may also be printed inline, while larger responses are summarized.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
