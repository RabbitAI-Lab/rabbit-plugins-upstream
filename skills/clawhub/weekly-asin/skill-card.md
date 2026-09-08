## Description:

在用户明确确认并完成报价后，结合单个已订阅 ASIN 的商品详情、快照和评论证据生成运营周报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon operators and ecommerce teams use this skill to request a confirmed weekly operations brief for one subscribed ASIN, based on ARI product detail, snapshot, and review evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give the agent broad authority over ARI billing, monitoring, exports, account confirmation settings, competitor tracking, and saved API key use.

Mitigation: Install only when that scope is intended; keep autoconfirm off or low, use quote-only language for price checks, and require explicit confirmation for paid or account-changing actions.

Risk: A custom ARI endpoint could redirect requests away from the official service.

Mitigation: Do not set ARI_ALLOW_CUSTOM_BASE unless intentionally using a trusted non-official ARI endpoint.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/weekly-asin)
- [Publisher profile](https://clawhub.ai/user/funewa)
- [Amazon ASIN 周报简报 专属运营工作流](references/operation-workflow.md)
- [ARI CLI 与 API 参考](references/reference.md)
- [ARI Amazon 评论智能助手使用指南](使用说明.md)
- [ARI API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI products](https://ari.funewa.com/zh/products)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, API Calls, Guidance]

**Output Format:** [Markdown prose with concise operational findings and optional CLI command references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include data range, ASIN/site, sample size, report identifier, credits used, and report URL when returned.]

## Skill Version(s):

1.4.8 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
