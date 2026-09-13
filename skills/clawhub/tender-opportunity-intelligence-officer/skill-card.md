## Description:

招投标商机情报与竞对动态分析助手，用于检索临期项目、拟建项目、招中标公告、企业画像、竞对动态和市场趋势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External business development, procurement, sales, and market-analysis users use this skill to find tender opportunities, monitor expiring or proposed projects, analyze competitors, and identify potential purchasers or suppliers from Zhiliaobiaoxun tender data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill calls a vendor API and may use or create a vendor API key.

Mitigation: Configure your own ZLBX_API_KEY when possible and install only if vendor API access is acceptable for the intended workflow.

Risk: Automatic registration can use a MAC-derived device identifier and store an API key in ~/.zlbx/config.json.

Mitigation: Use automatic registration only after explicit user consent; choose manual key configuration if device-derived registration or local plaintext key storage is not acceptable.

Risk: The skill can present vendor-controlled update notices, recharge links, or promotional redirects.

Mitigation: Treat those links and notices as vendor-provided content and review the destination before acting.

Risk: Contact details may be returned with account-tier masking or access controls.

Mitigation: Preserve masked values as returned, avoid attempting to reconstruct hidden contact data, and avoid bulk contact export unless authorized.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/tender-opportunity-intelligence-officer)
- [Publisher Profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [API Overview](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Account and API Key Portal](https://ai.zhiliaobiaoxun.com/?ch=s55)
- [Skill Documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [SKILL 自动注册详细流程](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with JSON request examples and occasional shell commands for API-key onboarding]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved auto-registration; API responses may include masked contact details depending on account tier.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
