## Description: <br>
This skill provides battle-tested guidance for integrating WeChat Mini Program payment and refund flows using Tencent CloudBase, covering cloud.cloudPay.unifiedOrder() for payments, cloud.cloudPay.refund() for refunds, cloud functions, CLI deployment, and critical pitfalls with fixes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jianqiaochen](https://clawhub.ai/user/jianqiaochen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to build, debug, and review WeChat Mini Program payment and refund flows on Tencent CloudBase. It is especially relevant when payments fall back to simulated mode, refunds silently fail, cloud-call access_token errors occur, or historical orders require refund backfill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Temporary refund recovery flows could trigger refunds without adequate authorization controls if copied into production. <br>
Mitigation: Limit any refund recovery tool to admin-only, server-authorized, idempotent, audited, eligibility-checked, and rate-limited use, then remove or disable it after the backfill is complete. <br>
Risk: Refund status can be recorded incorrectly if only wrapper-level success is checked. <br>
Mitigation: Require both CloudBase returnCode and WeChat Pay resultCode to be successful before updating order status, refund timestamps, or refund transaction identifiers. <br>


## Reference(s): <br>
- [CloudBase WeChat Pay gotchas](references/gotchas.md) <br>
- [ClawHub skill page](https://clawhub.ai/jianqiaochen/skills/cloudbase-wxpay) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JavaScript, JSON, WXML, and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes payment and refund workflow checks, deployment commands, environment variable guidance, and troubleshooting steps.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
