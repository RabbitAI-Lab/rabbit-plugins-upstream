## Description: <br>
汇付支付交易集成：用于聚合支付、托管支付、checkout-js、下单、查单、关单、退款、对账、支付通知、签名验签、请求头、幂等、交易终态、本地沙箱和支付上线；不用于企业/个人商户进件、图片上传、商户业务开通、商户详情或申请状态查询，这些任务使用 huifu-merchant-onboarding。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huifu](https://clawhub.ai/user/huifu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to integrate Huifu payment transactions, SDKs, hosted payment flows, checkout-js, refunds, reconciliation, notifications, signatures, idempotency, and production readiness checks while keeping merchant onboarding work out of scope. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill supports sensitive payment workflows, including refunds, order closure, reconciliation, webhooks, signatures, and production readiness. <br>
Mitigation: Use sandbox or test credentials first, keep production private keys and real payment data out of chats, logs, reports, and repositories, and review generated code before running it against production credentials. <br>
Risk: Incorrect handling of payment callbacks, synchronous returns, or checkout-js events can mark orders successful before the payment terminal state is confirmed. <br>
Mitigation: Confirm payment state with verified asynchronous notifications, idempotent status updates, and official query compensation before changing business order state. <br>
Risk: Some Java and PHP integration paths require transport-security and debug-logging checks before they are suitable for joint testing or production. <br>
Mitigation: Verify SDK transport security, reject unsafe PHP debug loaders, and keep private keys only in controlled server-side configuration before producing runnable joint-test or production code. <br>


## Reference(s): <br>
- [Huifu Skill Page](https://clawhub.ai/huifu/skills/huifu-pay-integration) <br>
- [Huifu Publisher Profile](https://clawhub.ai/user/huifu) <br>
- [汇付支付资料总览](artifact/references/shared-overview.md) <br>
- [官方服务资料源索引](artifact/references/official-service-source-index.md) <br>
- [凭据使用规则与存放边界](artifact/references/shared-credential-boundary.md) <br>
- [本地沙箱边界](artifact/references/shared-local-sandbox.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline code and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should cite the 3-5 task-relevant local reference files used and avoid production credentials, real payment data, fee conclusions, compliance conclusions, or channel approval conclusions.] <br>

## Skill Version(s): <br>
1.3.3 (source: server release evidence and artifact SKILL.md current version table) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
