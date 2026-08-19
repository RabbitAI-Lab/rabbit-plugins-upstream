## Description:

粤收付交易集成：用于聚合支付、托管支付、checkout-js、下单、查单、关单、退款、对账、支付通知、签名验签、请求头、幂等、交易终态、本地沙箱和支付上线；不用于企业/个人商户进件、图片上传、商户业务开通、商户详情或申请状态查询，这些任务使用 huifu-merchant-onboarding。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huanglin88](https://clawhub.ai/user/huanglin88)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical operations teams, and merchant integration staff use this skill to plan, generate, review, and troubleshoot 粤收付 payment integrations across common programming languages. It focuses on transaction APIs such as ordering, querying, closing, refunding, reconciliation, payment notifications, signatures, idempotency, sandbox testing, and production launch readiness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated examples may be adapted into code that touches real payment, refund, transfer, or cashout APIs.

Mitigation: Use sandbox credentials first and require human review before running code that moves money or issues refunds.

Risk: Merchant private keys or production credentials could be exposed during integration work.

Mitigation: Keep private keys and production credentials out of prompts and source control.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/huanglin88/payment-expert/tree/main/skills/cnyepay)
- [cnyepay ClawHub skill page](https://clawhub.ai/huanglin88/skills/cnyepay)
- [粤收付 Open Platform](https://open.cnyepay.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Configuration instructions]

**Output Format:** [Markdown with code examples and integration checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include payment API troubleshooting steps, signature and verification guidance, and language-specific sample code.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
