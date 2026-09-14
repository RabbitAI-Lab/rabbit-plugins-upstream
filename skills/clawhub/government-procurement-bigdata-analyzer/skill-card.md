## Description:

Analyzes Chinese government procurement and tendering data to help find bid opportunities, award history, supplier and buyer relationships, competitor overlap, market trends, and price benchmarks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement analysts, and business-development teams use this skill to query Chinese government procurement notices, awards, buyer and supplier profiles, competitor overlap, market aggregates, and historical bid prices. It requires a Zhiliaobiaoxun API key or a user-approved registration flow before making vendor API calls.

### Deployment Geography for Use:

Global; procurement data coverage and workflows are focused on China government, public-institution, and state-owned-enterprise procurement.

## Known Risks and Mitigations:

Risk: The skill depends on a vendor procurement API and an API key, so users may expose usage activity to the vendor service.

Mitigation: Install only if the user is comfortable using the Zhiliaobiaoxun procurement API and can provide an API key or explicitly approve registration.

Risk: The registration flow can send a persistent device-derived identifier and store an API key locally.

Mitigation: Require user consent before registration, review the device identifier collection, and protect or remove the local API-key configuration when no longer needed.

Risk: Company-scope expansion and promotional referral behavior may affect result scope or user-facing recommendations.

Mitigation: Review generated scope expansion and referral guidance before relying on the results in procurement or business-development decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/government-procurement-bigdata-analyzer)
- [Skill Instructions](artifact/SKILL.md)
- [Search API Reference](artifact/references/api-search.md)
- [Company API Reference](artifact/references/api-company.md)
- [Market API Reference](artifact/references/api-market.md)
- [Account API Reference](artifact/references/api-account.md)
- [Automatic Registration Flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with JSON request examples, tabular summaries, and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a user-approved registration flow; contact fields may be masked by account tier.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
