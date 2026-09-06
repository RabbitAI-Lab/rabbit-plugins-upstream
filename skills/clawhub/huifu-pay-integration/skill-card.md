## Description:

汇付支付集成 helps developers integrate and troubleshoot Huifu payment transaction flows across aggregation payments, hosted payments, checkout-js, order creation, payment queries, order closing, refunds, reconciliation, payment notifications, signing, idempotency, local sandbox checks, and go-live readiness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huifu](https://clawhub.ai/user/huifu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and integration engineers use this skill to choose the right Huifu payment product path, prepare SDK/API integration work, handle callbacks and final payment state, troubleshoot payment issues, and prepare go-live checks without exposing production secrets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment credentials, private keys, identity data, buyer IDs, or full payment logs could be exposed if users paste them into chat, logs, repositories, or generated examples.

Mitigation: Use sandbox or redacted values in prompts and examples, keep sandbox-credentials.json local and out of git, and store production secrets only in controlled server-side configuration.

Risk: Generated integration code could mishandle date preservation, redaction, encryption, retention, webhook verification, idempotency, or final payment state before联调 or production use.

Mitigation: Review generated code against the skill's payment notification, field preservation, credential boundary, and go-live checklist references before using it with real Huifu environments.

Risk: Local sandbox results could be mistaken for official联调 approval, production readiness, channel approval, risk-control approval, or settlement correctness.

Mitigation: Treat local sandbox output as a local protocol and state-machine rehearsal only, then confirm official联调, production credentials, notify_url reachability, monitoring, and channel readiness through Huifu's official process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huifu/skills/huifu-pay-integration)
- [汇付支付资料总览](references/shared-overview.md)
- [接入副驾驶向导](references/copilot-onboarding.md)
- [方案选择规则](references/copilot-solution-selection.md)
- [上线检查清单](references/copilot-go-live-checklist.md)
- [版权声明](references/shared-copyright-notice.md)
- [汇付官方网站](https://www.huifu.com/)
- [斗拱开放平台](https://paas.huifu.com/open/home/index.html)
- [基础参数汇总](https://paas.huifu.com/partners/api/doc/csfl/api_csfl.md)
- [名词解释](https://paas.huifu.com/partners/api/doc/csfl/api_csfl_mcjs.md)
- [返回码](https://paas.huifu.com/partners/api/doc/csfl/api_csfl_ywm.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with code snippets, configuration examples, and command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory integration guidance for agent users and are not self-executing.]

## Skill Version(s):

1.3.5 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
