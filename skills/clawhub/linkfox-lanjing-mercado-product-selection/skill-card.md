## Description:

Mercado Libre（美客多）选品数据查询与分析，通过 LinkFox 网关统一调用蓝鲸 24 个商品、官链、关键词、类目、趋势、店铺、评论、汇率与套餐用量工具，覆盖墨西哥、巴西、阿根廷、智利、哥伦比亚站点。当用户提到 Mercado Libre、美客多、蓝鲸选品、Lanjing、美客多选品、商品搜索、类目趋势、关键词热搜、流量词反查、店铺查询、评论查询、汇率、套餐用量时触发此技能。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce analysts use this skill to query and summarize Mercado Libre product, catalog, keyword, category, trend, seller, review, exchange-rate, and plan-usage data through LinkFox. It is intended for product-selection research across the documented Latin American marketplace sites.

### Deployment Geography for Use:

Global; Mercado Libre data coverage is documented for Mexico, Brazil, Argentina, Chile, and Colombia.

## Known Risks and Mitigations:

Risk: Mercado Libre query data and related parameters are sent to LinkFox services.

Mitigation: Install and use the skill only when LinkFox is trusted for this data, avoid unnecessary sensitive business inputs, and keep LINKFOX_* endpoint variables pointed at trusted HTTPS LinkFox hosts.

Risk: The skill includes phone-based onboarding and API key issuance flows.

Mitigation: Treat generated API keys as sensitive credentials, share only masked account details in conversation, and store environment variables securely.

Risk: Paid calls and payment order creation can incur user cost.

Mitigation: Confirm before paid tool calls or payment orders, use the documented free tools when sufficient, and rely on returned cost and package information before continuing.

Risk: Full API responses may be written to local linkfox/ session files.

Mitigation: Treat local response files as sensitive, limit unnecessary raw output, and protect or remove stored responses according to the user's data handling needs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-lanjing-mercado-product-selection)
- [Lanjing Mercado Libre Product Selection API reference](artifact/references/api.md)
- [Lanjing Mercado XP-MCP Tool Reference](artifact/references/lanjing-mercado-tool-reference.md)
- [LinkFox authentication and billing onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses or response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full LinkFox responses may be persisted under a local linkfox/ session data directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
