## Description:

工程建设招投标分析-建设通，当搜索词包含工程、施工、建筑、市政、监理、设计等建筑业专属词汇时触发，聚焦工程项目金额、中标单位资质背景，重点提取建筑类项目核心字段并进行业绩汇总。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business analysts use this skill to search construction bidding notices, retrieve bid details, summarize engineering project amounts, and analyze company bidding performance. It also supports market views such as top purchasers, suppliers, brands, price trends, and expiring project opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags under-disclosed account auto-registration, device fingerprint collection, and credential persistence.

Mitigation: Review before installing, configure ZLBX_API_KEY directly when possible, and approve auto-registration only when comfortable sending device-derived identifiers to the provider and storing the returned API key locally.

Risk: The skill can perform contact lookup and broad company-intelligence workflows.

Mitigation: Use contact lookup, company expansion, competitor discovery, and supplier recommendations only when the user explicitly requests that broader business-intelligence behavior.

Risk: API credentials are required for normal use and may be read from the environment or local agent configuration.

Mitigation: Do not ask users to paste API keys into chat, prefer environment or agent configuration, and avoid exposing stored credentials in responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/construction-tender-analyzer-jianshetong)
- [Publisher profile](https://clawhub.ai/user/pkuycl)
- [API account reference](references/api-account.md)
- [API company reference](references/api-company.md)
- [API market reference](references/api-market.md)
- [API search reference](references/api-search.md)
- [Auto-registration reference](references/auto-register.md)
- [Jianshetong API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/{工具名})
- [Jianshetong account portal](https://ai.zhiliaobiaoxun.com/?ch=s33)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown narrative with JSON request examples, command snippets, and structured analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ZLBX_API_KEY or a locally stored API key to call the Jianshetong tender-analysis API; responses may include tender records, company profiles, market aggregates, account balance data, and contact information.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
