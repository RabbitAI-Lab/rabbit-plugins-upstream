## Description:

Provides YueShouFu/CNYEPay payment integration guidance for aggregate payments, hosted payments, checkout-js, order creation and lookup, order closure, refunds, reconciliation, payment notifications, RSA2 signing and verification, request headers, idempotency, terminal states, sandbox testing, and production launch readiness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huanglin88](https://clawhub.ai/user/huanglin88)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical operators, and merchant integration teams use this skill to integrate YueShouFu/CNYEPay payment APIs across payment, refund, reconciliation, webhook, signing, sandbox, and production-readiness workflows. It is scoped to API integration guidance and excludes merchant onboarding, account or key application, image upload, and merchant status workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated refund, transfer, cashout, or signing code could affect funds if used directly in production.

Mitigation: Test generated code in a sandbox, review endpoint selection and amount handling, and require human approval before using production credentials or moving funds.

Risk: Payment signing and webhook verification examples may expose private keys or weaken transaction validation if adapted incorrectly.

Mitigation: Protect private keys, verify callbacks with the platform public key, enforce idempotency, and review all signing and verification code before deployment.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/huanglin88/payment-expert/tree/main/skills/cnyepay)
- [ClawHub skill page](https://clawhub.ai/huanglin88/skills/payment-expert)
- [YueShouFu/CNYEPay API documentation](https://open.cnyepay.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code snippets, API examples, troubleshooting steps, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include high-impact payment, refund, transfer, cashout, and signing examples that require sandbox testing and human review before production use.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
