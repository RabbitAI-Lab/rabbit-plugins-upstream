## Description:

招中标数据智能体为 AI Agent 提供招投标公告检索、标讯详情获取、企业画像、竞争对手识别、市场聚合统计与价格趋势分析能力。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent builders use this skill to retrieve and analyze bidding, procurement, supplier, company, and market data for sourcing, sales intelligence, competitive analysis, and structured procurement reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform account signup, local credential storage, and device fingerprinting during auto-registration.

Mitigation: Prefer setting ZLBX_API_KEY yourself; if auto-registration is used, require user consent before collecting platform, architecture, and hashed MAC address, and store the returned API key locally with clear provenance.

Risk: Company contact lookups can return sensitive personal contact details.

Mitigation: Treat returned contact data as sensitive, preserve masking when contact_privacy is masked, do not attempt to fill masked numbers from other sources, and avoid bulk export.

Risk: Shorthand company names can resolve to the wrong organization or scope.

Mitigation: Confirm the resolved company scope when shorthand or ambiguous names are used, especially before presenting company profiles, partner lists, contacts, or competitor analysis.

Risk: Amount fields use different units across APIs, which can produce misleading filters or reports.

Mitigation: Check each tool's documented amount unit before calling it and normalize displayed monetary values with explicit units.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/bid-data-intelligent-agent)
- [API overview and usage guide](artifact/SKILL.md)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Auto-registration flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown responses with JSON request examples, tables, links, and structured analysis.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved auto-registration before authenticated data queries.]

## Skill Version(s):

1.0.3 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
