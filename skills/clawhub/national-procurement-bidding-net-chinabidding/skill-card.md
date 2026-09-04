## Description:

Provides procurement and bidding search, company analysis, market aggregation, price trends, and account lookups for China's procurement and bidding data through the Zhiliaobiaoxun API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Chinese procurement and bidding notices, inspect company bidding history, identify buyers and suppliers, analyze markets, and check account usage. It helps agents turn procurement questions into API-backed searches, summaries, and follow-up analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement queries are sent to the third-party vendor service.

Mitigation: Install only when the user or organization is comfortable sharing procurement search terms and analysis requests with the publisher.

Risk: If no API key is configured, the skill can register a device-based trial account and store an API key locally.

Mitigation: Preconfigure ZLBX_API_KEY to avoid auto-registration, require user consent before registration, and review ~/.zlbx/config.json for stored keys.

Risk: Returned project contact information may include sensitive business contact details.

Mitigation: Handle contact data carefully, avoid exposing API keys, and do not attempt to bypass service-side masking of contact information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/national-procurement-bidding-net-chinabidding)
- [Search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with JSON request examples, result summaries, links, and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZLBX_API_KEY or local configuration; may create and store a trial API key only after user consent when no key is configured.]

## Skill Version(s):

1.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
