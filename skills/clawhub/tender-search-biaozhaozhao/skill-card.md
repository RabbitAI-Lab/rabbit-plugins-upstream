## Description:

招投标快捷检索引擎-标找找，当用户需要快速查询特定关键词的招标或中标公告时调用，优先调用基础搜索工具提取项目名称、金额和链接，输出精简直接的列表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement and business-development users use this skill to search tender and award notices, inspect company bidding activity, and summarize market, competitor, supplier, purchaser, brand, price, and account status information from the Biaozhaozhao API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retrieve broad procurement intelligence and project contact data.

Mitigation: Limit use to appropriate procurement or business-analysis purposes, avoid exposing unnecessary contact details, and verify sensitive results against the linked source records before acting on them.

Risk: The skill may use device-linked auto-registration and local credential storage when no API key is configured.

Mitigation: Configure ZLBX_API_KEY manually to avoid auto-registration, or require explicit user consent before collecting the documented device attributes and storing the returned API key.

Risk: The skill can generate recharge or auto-login links when account balance is exhausted.

Mitigation: Check that links point to the expected zhiliaobiaoxun.com domain, explain the quota or payment context, and avoid sharing generated session links beyond the active user workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/tender-search-biaozhaozhao)
- [Publisher profile](https://clawhub.ai/user/liu-jiapeng)
- [Biaozhaozhao API documentation](https://ai.zhiliaobiaoxun.com/docs/api/)
- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [SKILL 自动注册详细流程](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise search result lists, JSON-style API request examples, setup commands, and operational guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based auto-registration; responses may include tender links, project contact information, balance status, recharge links, or auto-login links.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
