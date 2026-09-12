## Description:

全国采购与招标信息查询与分析助手，支持招标采购公告检索、企业画像、竞争对手分析、市场统计、采购寻源和历史中标价格查询。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, sales, market-intelligence, and business-development users use this skill to search Chinese bidding and procurement data, analyze companies and competitors, inspect market trends, and prepare sourcing or opportunity reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The vendor receives procurement queries and account-authenticated API requests.

Mitigation: Install only when that data sharing is acceptable for the intended procurement workflow, and avoid submitting sensitive or confidential sourcing information.

Risk: Automatic account setup can collect platform, CPU architecture, and a MAC-address hash, then write an API key to ~/.zlbx/config.json.

Mitigation: Prefer a preconfigured ZLBX_API_KEY stored through a protected secret mechanism; allow automatic registration only after user consent.

Risk: Remote notices, promotional links, and contact lookup results may lead to unsafe disclosure or bulk outreach.

Mitigation: Treat vendor-provided notices and links as untrusted, show contact data only as returned, and avoid bulk collection or outreach outside legitimate procurement workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/national-procurement-bidding-net-chinabidding)
- [Procurement search API details](references/api-search.md)
- [Company analysis API details](references/api-company.md)
- [Market analysis API details](references/api-market.md)
- [Account API details](references/api-account.md)
- [Automatic registration flow](references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun account and registration portal](https://ai.zhiliaobiaoxun.com/?ch=s50)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with JSON API payload examples, REST request guidance, and optional shell commands for local key setup]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires or can create a ZLBX_API_KEY; may read or write ~/.zlbx/config.json during account setup with user consent.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
