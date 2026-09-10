## Description:

Analyzes smart transportation, rail transit, road, ETC, signaling, and traffic equipment procurement opportunities using bid, award, company, market, and price data from 知了标讯.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Chinese transportation infrastructure bid notices, analyze bidders and competitors, identify procurement opportunities, and summarize market trends for smart transit and rail-related categories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party bid-data service for search, company, market, account, and registration operations.

Mitigation: Install and use it only when that service relationship is acceptable, and avoid submitting sensitive internal procurement plans unless approved.

Risk: The skill may read or create a local API-key config when no API key is already configured.

Mitigation: Prefer supplying ZLBX_API_KEY through a managed environment or secure credential store, and do not expose the API key in chat or logs.

Risk: If no key is configured, the skill can ask to create a free account using platform, CPU architecture, and a hashed MAC address for device de-duplication.

Mitigation: Require explicit user consent before account creation or device-feature collection, and use the manual account path if that collection is not acceptable.

Risk: The security summary flags promotional referral behavior that users should review first.

Mitigation: Review referral links and account-upgrade prompts before deployment, and document an approved account acquisition path for production users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/smart-transit-rail-bid-analyzer)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Market API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request examples, HTTP commands, and summarized API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a user-approved free-account registration flow; API responses are JSON and may include masked contact data for free or trial accounts.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
