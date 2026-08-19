## Description:

Helps agents search and analyze Chinese tender, procurement, company, supplier, competitor, pricing, and expiring-project opportunity data through the 标标达 API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, sales, and bid teams use this skill to find relevant tender opportunities, assess bid feasibility, check potential bid-control risks, analyze competitors and suppliers, and review historical award pricing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The provider receives procurement queries sent through the skill's API.

Mitigation: Install only when the user or organization is comfortable sharing procurement queries with this third-party provider.

Risk: If no API key is configured, the trial signup flow may collect OS, CPU architecture, and a hashed MAC-derived device identifier and send them to the provider.

Mitigation: Prefer configuring ZLBX_API_KEY manually before use, and decline automatic registration when device-based trial signup is not acceptable.

Risk: Automatic registration can persist an API key in ~/.zlbx/config.json.

Mitigation: Review or remove ~/.zlbx/config.json if persistent local credentials are not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/tender-opportunity-biaobiaoda)
- [Publisher profile](https://clawhub.ai/user/liu-jiapeng)
- [标讯搜索类工具 API 详情](artifact/references/api-search.md)
- [企业分析类工具 API 详情](artifact/references/api-company.md)
- [市场分析类工具 API 详情](artifact/references/api-market.md)
- [账户查询类工具 API 详情](artifact/references/api-account.md)
- [SKILL 自动注册详细流程](artifact/references/auto-register.md)
- [API key portal](https://ai.zhiliaobiaoxun.com/?ch=s26)
- [标标达 API base URL](https://mcp-server.zhiliaobiaoxun.com/api_v2/{工具名})

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with API request guidance, JSON examples, and occasional shell or configuration commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a locally saved ~/.zlbx/config.json API key for authenticated API access.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
