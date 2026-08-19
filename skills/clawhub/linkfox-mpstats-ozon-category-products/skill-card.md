## Description:

Drills into Ozon Russia products under a full Russian category path and returns SKU-level sales, revenue, price, rating, stock, turnover, lost-profit, ranking, and brand metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace analysts, ecommerce operators, and agent users use this skill to inspect Ozon category-level SKU performance, identify bestsellers or blue-ocean opportunities, and compare brands within a specific category path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends marketplace analytics queries to LinkFox services and may store result files or cache data locally.

Mitigation: Install only if LinkFox is trusted with the queried marketplace data, and periodically clean local linkfox output and cache files when results are sensitive.

Risk: The onboarding flow can handle phone/SMS login, generated API keys, billing package actions, and payment ordering.

Mitigation: Prefer self-service API key setup when possible, and review any plan selection or payment step before approving it.

Risk: The evidence security summary notes silent feedback reporting behavior that needs careful review.

Mitigation: Review feedback content and reporting behavior before deployment, especially in environments with sensitive user prompts or business data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-mpstats-ozon-category-products)
- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request examples, shell command examples, and JSON API responses or response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes complete API responses to local linkfox session data files; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
