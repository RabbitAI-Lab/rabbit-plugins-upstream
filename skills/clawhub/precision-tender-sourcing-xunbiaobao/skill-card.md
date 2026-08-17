## Description:

精准寻标与获客引擎-寻标宝，当用户需要通过招投标数据进行客户拓展、寻找潜在采购单位或分析企业上下游时调用，重点调用企业合作客户及供应商查询接口，输出清晰的获客目标列表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External business development, sales, procurement, and market-analysis teams use this skill to search tender data, identify potential buyers or suppliers, analyze company relationships, and produce prioritized outreach targets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes auto-registration behavior that can derive a device identifier from platform, CPU architecture, and a hashed MAC address, send it to a remote service, and store an API key locally.

Mitigation: Review before installation, configure ZLBX_API_KEY manually to avoid auto-registration, and require explicit user consent before any device-feature collection or registration request.

Risk: Company contacts, partner relationships, and tender-derived outreach targets may include sensitive business or personal data.

Mitigation: Use returned contact and relationship data only for authorized, lawful outreach or analysis, and avoid exposing API keys or sensitive returned records in shared logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/precision-tender-sourcing-xunbiaobao)
- [Tender search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration behavior](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Configuration]

**Output Format:** [Markdown responses with JSON request examples, shell commands, and structured business-analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or agent configuration; may call external Zhiliaobiaoxun APIs and may store an API key locally after user-approved trial registration.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
