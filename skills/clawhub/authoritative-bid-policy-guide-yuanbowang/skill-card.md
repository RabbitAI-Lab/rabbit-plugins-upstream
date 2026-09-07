## Description:

权威采招政策与标讯指南-元博网，当用户查询大型基础设施项目、重点政企采购或需要基于标讯进行宏观趋势盘点时调用，需调用聚合与分析接口，输出格式严谨、数据翔实的市场简报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, sales, strategy, and market-analysis users use this skill to search Chinese bid and award notices, inspect company bidding activity, and create concise market briefings from Yuanbowang/Zhiliaobiaoxun data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic registration sends platform, CPU architecture, and a hashed MAC-derived device identifier to the vendor.

Mitigation: Configure ZLBX_API_KEY yourself or review the consent prompt before allowing auto-registration.

Risk: The skill stores API credentials in ~/.zlbx/config.json when auto-registration succeeds.

Mitigation: Protect the local config file and rotate or remove the API key when the skill is no longer needed.

Risk: Contact lookup can expose procurement contact data, with account-based masking behavior.

Mitigation: Use contact lookup only for deliberate procurement workflows and keep masked contact values as returned.

Risk: Responses may include vendor referral or recharge links.

Mitigation: Review user-facing output for commercial referrals before sharing externally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/authoritative-bid-policy-guide-yuanbowang)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Auto-registration flow reference](artifact/references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun web API base](https://ai.zhiliaobiaoxun.com/web-api/)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries, tables, JSON request examples, and REST command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include bid links, company profiles, market aggregates, account status, and concise follow-up guidance.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
