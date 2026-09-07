## Description:

医疗大健康采招雷达-医疗招标采购网，当搜索词包含医院、医疗、卫生、体检时触发，重点提取采购方（医院）和中标方（医药公司/代理商），分析特定医院的Top供应商体系。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement analysts, and business-development teams use this skill to search medical and healthcare procurement notices, identify purchasing hospitals and awarded suppliers, and analyze top supplier relationships for specific hospitals.

### Deployment Geography for Use:

Global; the documented data and APIs focus on Chinese bidding and procurement records.

## Known Risks and Mitigations:

Risk: Opt-in registration sends a device-derived MAC hash to the vendor.

Mitigation: Use a manually provisioned ZLBX_API_KEY through a secure secret mechanism when device-derived registration is not acceptable.

Risk: Auto-registration can persist an API key in ~/.zlbx/config.json.

Mitigation: Review local credential storage and file permissions, or provide ZLBX_API_KEY through the agent's secret management instead.

Risk: The skill can return procurement contacts and account-related data through vendor APIs.

Mitigation: Use it only for procurement workflows, respect masked contact responses, and avoid bulk contact harvesting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thuanlynham-stack/skills/medical-health-bid-radar-yiliaozhaobiaocaigouwang)
- [Publisher profile](https://clawhub.ai/user/thuanlynham-stack)
- [Skill instructions](artifact/SKILL.md)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Auto-registration reference](artifact/references/auto-register.md)
- [Zhiliaobiaoxun data API](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun account portal](https://ai.zhiliaobiaoxun.com/?ch=s36)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Configuration]

**Output Format:** [Markdown with tables, JSON request examples, and REST command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or opt-in auto-registration before data queries.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
