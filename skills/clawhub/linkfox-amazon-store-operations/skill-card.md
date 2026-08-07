## Description:

亚马逊店铺 SP-API 运营一站式 AI 工具集，整合授权、订单、Listing、定价、Catalog、报告、Feeds、买家反馈、文件上传和 A+ Content 等能力，覆盖店铺日常运营链路。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, operators, and developers use this skill to authorize stores and run SP-API-backed workflows for orders, listings, pricing, catalog lookup, reports, feeds, buyer feedback, uploads, and A+ Content.

### Deployment Geography for Use:

Amazon marketplace regions supported by the configured seller authorization, including North America, Europe, and Far East marketplaces.

## Known Risks and Mitigations:

Risk: Amazon API keys, access tokens, seller account data, order data, reports, and listing details may pass through the LinkFox gateway and be written to local output folders.

Mitigation: Install only when the publisher is trusted for Amazon seller operations, protect credential environment variables, avoid inline output for token-bearing responses, and review local linkfox output folders after use.

Risk: The skill can perform write actions such as listing changes, feed uploads, A+ Content updates, and shipment updates.

Mitigation: Require explicit user confirmation before write actions and verify marketplace, seller, SKU, ASIN, feed, shipment, and content parameters before execution.

Risk: Gateway URLs can be controlled by environment variables, which could route authenticated requests to an unintended endpoint.

Mitigation: Use the default LinkFox gateway and avoid untrusted overrides for gateway-related environment variables.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-operations)
- [亚马逊店铺授权快速开始指南](references/quick-start.md)
- [亚马逊店铺授权流程详细说明](references/authorization-flow.md)
- [亚马逊店铺授权与管理](references/linkfox-amazon-store-auth.md)
- [亚马逊店铺订单](references/linkfox-amazon-store-orders.md)
- [亚马逊店铺 Listings 与相关 API](references/linkfox-amazon-store-listings.md)
- [亚马逊店铺报告获取](references/linkfox-amazon-store-report.md)
- [Amazon Store 完整报告类型参考](references/report-types.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with JSON parameters and shell command examples; scripts emit JSON responses or concise summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses may be saved under the working directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.2.1 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
