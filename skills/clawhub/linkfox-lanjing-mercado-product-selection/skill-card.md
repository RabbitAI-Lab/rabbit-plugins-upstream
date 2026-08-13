## Description:

Mercado Libre（美客多）选品数据查询与分析，通过 LinkFox 网关统一调用蓝鲸 24 个商品、官链、关键词、类目、趋势、店铺、评论、汇率与套餐用量工具，覆盖墨西哥、巴西、阿根廷、智利、哥伦比亚站点。当用户提到 Mercado Libre、美客多、蓝鲸选品、Lanjing、美客多选品、商品搜索、类目趋势、关键词热搜、流量词反查、店铺查询、评论查询、汇率、套餐用量时触发此技能。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, analysts, and developers use this skill to query Mercado Libre product-selection data through LinkFox, including products, catalogs, keywords, categories, trends, sellers, reviews, exchange rates, and plan usage. It supports research across Mexico, Brazil, Argentina, Chile, and supported Colombia workflows while helping the agent choose the correct tool and parameters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox account credentials, phone/SMS login data, and API keys.

Mitigation: Use it only in trusted workspaces, keep generated API keys out of chat and logs, and keep LINKFOX_* endpoint variables pointed at trusted LinkFox hosts.

Risk: Paid Mercado data tools can spend account credits or create billing flows.

Mitigation: Confirm paid calls and billing actions with the user before continuing, especially for repeated searches, pagination, keyword changes, or payment-order creation.

Risk: Full Mercado/API responses are saved to local LinkFox session files and may contain sensitive business data.

Mitigation: Run the skill only where saved response files are acceptable, avoid sharing full raw payloads, and summarize or extract only needed fields for user-facing output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-lanjing-mercado-product-selection)
- [LinkFox Skills](https://skill.linkfox.com/)
- [LinkFox Gateway API Reference](references/api.md)
- [Lanjing Mercado XP-MCP Tool Reference](references/lanjing-mercado-tool-reference.md)
- [Authentication and Billing Onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON API responses, saved response files, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The main script saves full responses under a LinkFox session data directory, prints full JSON for small responses, summarizes large responses, and caches same-parameter calls for 24 hours by default.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
