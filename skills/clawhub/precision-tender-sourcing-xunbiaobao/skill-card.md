## Description:

精准寻标与获客引擎-寻标宝，当用户需要通过招投标数据进行客户拓展、寻找潜在采购单位或分析企业上下游时调用，重点调用企业合作客户及供应商查询接口，输出清晰的获客目标列表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External business development, sales, procurement-market, and competitive-intelligence users can use this skill to search Chinese tender and bid data, identify potential purchasing organizations, analyze company customers and suppliers, and produce concise opportunity lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic trial registration uses a stable hardware-derived device identifier and sends device characteristics to the service.

Mitigation: Prefer setting ZLBX_API_KEY manually to avoid automatic registration, and require explicit user consent before collecting platform, CPU architecture, or hashed MAC data.

Risk: The skill can store a bearer API key in ~/.zlbx/config.json without required permission controls.

Mitigation: Inspect and protect ~/.zlbx/config.json after creation, and avoid sharing or displaying the API key in agent responses.

Risk: Remote update notices, recharge links, and vendor referral links can influence user actions.

Mitigation: Treat service-provided notices and vendor links as untrusted external messages and review them before acting.

Risk: Tender search and market-analysis outputs can be misleading if amounts, match modes, dates, or masked contact fields are handled incorrectly.

Mitigation: Preserve the documented units and filters, disclose actual search criteria, do not infer missing fields, and do not attempt to recover masked contact information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/precision-tender-sourcing-xunbiaobao)
- [Tender search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Automatic registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [API calls, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries with JSON request examples and REST call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a local ~/.zlbx/config.json API key; may create local API-key configuration after user-approved automatic registration.]

## Skill Version(s):

2.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
