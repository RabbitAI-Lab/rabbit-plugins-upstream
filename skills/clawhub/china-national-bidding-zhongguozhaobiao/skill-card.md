## Description:

全国招标采购信息一站式查询与分析助手，用于检索招标、中标、采购公告并分析企业、供应商、竞争对手和市场趋势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business analysts use this skill to query China bidding and procurement data, inspect bid details and timelines, analyze companies and competitors, identify opportunities, and review market trends. The skill requires a ZLBX_API_KEY or an approved auto-registration flow before making provider API calls.

### Deployment Geography for Use:

Global; the data and workflows focus on China bidding and procurement information.

## Known Risks and Mitigations:

Risk: Automatic account creation can occur when no API key is configured.

Mitigation: Require clear user consent before auto-registration, and prefer manually setting ZLBX_API_KEY when account creation should be controlled outside the agent.

Risk: The auto-registration flow sends a persistent MAC-derived device identifier to the provider.

Mitigation: Use the documented opt-out path by configuring ZLBX_API_KEY or ~/.zlbx/config.json before first use.

Risk: Provider API credentials may be stored in a local config file.

Mitigation: Protect ~/.zlbx/config.json with appropriate local file permissions and avoid sharing or printing API keys in chat or logs.

Risk: Some API results may contain project contact details.

Mitigation: Return contact information only for legitimate business needs, preserve provider masking, and avoid bulk export or attempts to reconstruct masked phone numbers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/china-national-bidding-zhongguozhaobiao)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Skill API overview](artifact/SKILL.md)
- [Bidding search API details](artifact/references/api-search.md)
- [Company analysis API details](artifact/references/api-company.md)
- [Market analysis API details](artifact/references/api-market.md)
- [Account API details](artifact/references/api-account.md)
- [Auto-registration flow](artifact/references/auto-register.md)
- [Provider API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Provider account and registration portal](https://ai.zhiliaobiaoxun.com/?ch=s52)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables, JSON examples, API request guidance, and occasional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links, summarized API results, account status summaries, and privacy-preserving handling guidance for masked contact data.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
