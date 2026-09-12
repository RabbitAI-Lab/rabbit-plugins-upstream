## Description:

招投标大数据 AI 分析平台，用自然语言完成市场分析、商机研判与趋势预测：多维聚合统计（月/季/年/省份/行业/品牌）、Top采购单位/中标单位/中标品牌、历史中标价格走势、潜在中标候选预测。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query and analyze bidding, tender, procurement, company, competitor, market-share, opportunity, and pricing data from the Zhiliaobiaoxun bidding-data platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic onboarding can send a stable MAC-derived device hash to the vendor.

Mitigation: Prefer a user-provided ZLBX_API_KEY; if auto-registration is needed, require explicit user consent before collecting platform, CPU architecture, and MAC hash.

Risk: The skill can create and store an API key in ~/.zlbx/config.json.

Mitigation: Review file permissions on ~/.zlbx/config.json and avoid displaying or sharing API keys in chat output.

Risk: Generated auto-login or recharge links can provide account access.

Mitigation: Treat generated login and recharge links as sensitive, time-bound account links and avoid exposing them outside the active user session.

Risk: Contact data may be account-tiered and can include masked phone numbers.

Mitigation: Display contact fields as returned, do not attempt to deanonymize masked phone numbers, and avoid bulk exporting contacts.

## Reference(s):

- [Skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/ai-bidding-data-platform)
- [Account API reference](references/api-account.md)
- [Company API reference](references/api-company.md)
- [Market API reference](references/api-market.md)
- [Search API reference](references/api-search.md)
- [Auto-registration reference](references/auto-register.md)
- [Bidding data API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun AI platform](https://ai.zhiliaobiaoxun.com/?ch=s133)
- [Zhiliaobiaoxun bidding agent](https://agent.zhiliaobiaoxun.com?utm_source=skill)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with REST request guidance, JSON examples, tabular summaries, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based auto-registration before data API calls; account queries are free, while data queries consume vendor quota.]

## Skill Version(s):

1.0.4 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
