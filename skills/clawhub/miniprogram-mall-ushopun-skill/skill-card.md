## Description:

基于 Ushopun（优社云AI）官方 miniProgramV2 真实项目构建的微信小程序商城前端，覆盖首页、分类、商品详情、购物车、结算、订单、个人中心等 50+ 页面与完整交易链路，并提供 dev.ushopun.com OpenAPI 对接规范与调用示例。

This skill is ready for commercial/non-commercial use.

## Publisher:

[urselect](https://clawhub.ai/user/urselect)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to generate or adapt native WeChat mini-program mall front ends for Ushopun-backed storefronts. It supports the core commerce flow across catalog, product detail, cart, checkout, orders, account pages, payments, coupons, points, wallet, distribution, reviews, and related Ushopun OpenAPI integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated code may handle connector ApiTokens, JWT tokens, phone numbers, passwords, addresses, wallet payout details, and payment or order actions.

Mitigation: Keep credentials and sensitive user data in placeholders, environment variables, or runtime configuration, and avoid writing them into generated source files.

Risk: Generated workflows may submit orders, payments, withdrawals, posts, or private messages against a live Ushopun tenant.

Mitigation: Require explicit user confirmation before code paths perform commerce, payout, content posting, or messaging actions.

Risk: Some Ushopun modules may be unavailable for a tenant or require account enablement.

Mitigation: Check module availability and API reachability on the Ushopun development or tenant environment before relying on generated flows.

## Reference(s):

- [Ushopun OpenAPI specification](artifact/openapi.json)
- [Ushopun development site](https://dev.ushopun.com)
- [Server-resolved source repository](https://github.com/urselect/miniprogram-mall-ushopun-skill)
- [ClawHub skill release page](https://clawhub.ai/urselect/skills/miniprogram-mall-ushopun-skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown with JavaScript, JSON, WXML, WXSS, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose multi-file native WeChat mini-program page structures and Ushopun API integration patterns.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
