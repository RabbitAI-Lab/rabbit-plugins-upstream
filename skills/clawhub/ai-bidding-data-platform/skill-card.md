## Description:

招投标大数据 AI 分析平台，用自然语言完成市场分析、商机研判与趋势预测，包括多维聚合统计、Top 采购单位和中标单位分析、历史中标价格走势、潜在中标候选预测等招投标数据分析任务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External business-development, sales, market-analysis, and procurement users use this skill to query and analyze Chinese bidding and award data, company procurement activity, market share, price trends, expiring projects, and proposed projects through the ZLBX API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bidding and company-analysis queries are sent to a third-party vendor service.

Mitigation: Install only when that data flow is acceptable for the intended business use, and avoid submitting sensitive queries unless approved.

Risk: The skill uses a ZLBX_API_KEY and can store an auto-registered key in ~/.zlbx/config.json.

Mitigation: Prefer a user-managed API key when possible, protect the key as a credential, and do not expose it in chat or logs.

Risk: Auto-registration sends a MAC-derived hash and other minimal device features for trial-account deduplication.

Mitigation: Require user consent before auto-registration, and use manual key configuration if device privacy is a concern.

Risk: Returned contact names and phone numbers may be sensitive business or personal data.

Mitigation: Handle contact data as sensitive, preserve masking when returned by the service, and avoid bulk export or enrichment.

Risk: Referral, recharge, and promotional links are part of vendor account flows.

Mitigation: Treat those links as optional vendor flows, not required analysis results, and present them only when relevant.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/ai-bidding-data-platform)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [API overview and operating guide](artifact/SKILL.md)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Auto-registration flow](artifact/references/auto-register.md)
- [ZLBX data API base URL](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZLBX account and registration portal](https://ai.zhiliaobiaoxun.com/?ch=s133)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with REST API request examples, JSON payloads, tables, and concise bidding-data analysis.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-consented auto-registration; may store an API key in ~/.zlbx/config.json.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
