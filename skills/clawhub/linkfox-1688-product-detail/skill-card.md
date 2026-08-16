## Description:

1688 商品详情查询。通过 offerId 获取商品标题、属性、SKU/库存、批发价和外币价、起批量、图片/视频、物流包装、供应商服务、混批、发票与证书等采购信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and sourcing teams use this skill to retrieve live 1688 product detail records for a known offer ID, including SKU pricing and stock, MOQ, logistics, supplier metrics, media, invoices, and certificates. It supports product and supplier fact review for cross-border purchasing decisions but does not discover products or place orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill combines 1688 product lookup with account setup, API-key issuance, billing, payment-order creation, feedback reporting, and persistent local storage.

Mitigation: Install only if those LinkFox account and billing workflows are acceptable for the deployment, and prefer self-service login and payment through LinkFox's website when possible.

Risk: Product lookup requests and saved responses may include sensitive product, supplier, pricing, or sourcing information.

Mitigation: Review configured LINKFOX_* endpoints before use and periodically clean the local linkfox response and cache directory when the data is sensitive.

Risk: SMS-code based onboarding can expose account authorization material to an agent workflow.

Mitigation: Avoid sharing SMS codes with an agent unless necessary, and use an already provisioned API key or LinkFox's self-service console when available.

## Reference(s):

- [1688 商品详情 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-1688-product-detail)
- [LinkFox Skills](https://skill.linkfox.com/)
- [LinkFox agent console](https://agent.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON product data or summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The lookup script writes full API responses to a local linkfox session data directory and prints either full JSON for small responses or a summary for larger responses.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
