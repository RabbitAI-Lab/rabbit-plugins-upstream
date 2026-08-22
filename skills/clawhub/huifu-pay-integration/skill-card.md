## Description:

汇付支付交易集成：用于聚合支付、托管支付、checkout-js、下单、查单、关单、退款、对账、支付通知、签名验签、请求头、幂等、交易终态、本地沙箱和支付上线；不用于企业/个人商户进件、图片上传、商户业务开通、商户详情或申请状态查询，这些任务使用 huifu-merchant-onboarding。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huifu](https://clawhub.ai/user/huifu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and payment-integration engineers use this skill to choose Huifu payment product lines, route to the right local references, and produce integration, testing, terminal-state, notification, refund, reconciliation, and go-live guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Merchant keys, sandbox credential exports, buyer identifiers, ID numbers, IP addresses, and bank-card-related fields may be exposed if copied into prompts, logs, repositories, or frontend code.

Mitigation: Keep credentials and sensitive payment data server-side, store secrets in environment variables, CI/CD secret stores, or a key-management system, redact logs, and use test or sandbox credentials outside controlled production deployments.

Risk: Payment callbacks or frontend returns may be mistaken for terminal payment state.

Mitigation: Verify Huifu notifications, apply idempotency, confirm payment or refund status with official query flows, and update business state only after the server-side terminal-state checks pass.

Risk: Generated integration examples may be applied to the wrong Huifu product line, endpoint, SDK, or merchant environment.

Mitigation: Confirm product line, endpoint, integration stage, technology stack, merchant identifiers, notification URL, and SDK version before using generated code or configuration in testing or production.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huifu/skills/huifu-pay-integration)
- [Skill Definition](artifact/SKILL.md)
- [Official Service Source Index](artifact/references/official-service-source-index.md)
- [Shared Overview](artifact/references/shared-overview.md)
- [Server SDK Matrix](artifact/references/shared-server-sdk-matrix.md)
- [Asynchronous Notification Rules](artifact/references/shared-async-notify.md)
- [Credential Boundary](artifact/references/shared-credential-boundary.md)
- [Copyright Notice](artifact/references/shared-copyright-notice.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code blocks, command snippets, configuration examples, and reference lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers should name the selected product line, integration stage, technology stack, actual references used, terminal-state boundaries, missing inputs, and next steps.]

## Skill Version(s):

1.3.4 (source: server release evidence and artifact SKILL.md current version table)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
