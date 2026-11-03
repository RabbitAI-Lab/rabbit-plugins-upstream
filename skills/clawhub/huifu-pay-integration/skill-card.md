## Description:

Helps developers integrate and troubleshoot Huifu payment flows, account queries, checkout, and notifications using Java, PHP, or Python.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huifu](https://clawhub.ai/user/huifu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and payment engineers use this skill to implement Huifu payment and account-query workflows, investigate integration issues, and prepare safe production handoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server security evidence flags insecure payment connection guidance and conflicting advice about collecting sensitive customer information.

Mitigation: Require engineering review before production credentials are connected, verify certificate and hostname checks before live traffic, and use masked or synthetic customer data.

Risk: Payment and refund operations, signing keys, and stored callback payloads can expose sensitive financial operations or information.

Mitigation: Explicitly authorize payment and refund operations, keep signing keys in protected local configuration, and restrict access to and retention of callback payloads.

Risk: External SDKs and optional sandbox executables are outside the artifact security review.

Mitigation: Verify their versions and integrity before running them, and close testing tunnels when finished.

## Reference(s):

- [Huifu payment integration guide](https://paas.huifu.com/open/service/develop/#/)
- [Huifu Partner API documentation](https://paas.huifu.com/partners/api/doc/)
- [Huifu account balance query API](https://paas.huifu.com/partners/api/doc/jyjs/api_jyjs_yuexxcx.md)
- [Huifu account ledger query API](https://paas.huifu.com/partners/api/doc/yuer/api_acctlscx.md)
- [Huifu account ledger summary API](https://paas.huifu.com/partners/api/doc/zhy/api_acct_log_summary.md)
- [ClawHub skill release](https://clawhub.ai/huifu/skills/huifu-pay-integration)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Code, Configuration, Shell commands]

**Output Format:** [Markdown with API field guidance, code examples, and integration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tailored to the selected Huifu product, interface, and programming language.]

## Skill Version(s):

1.5.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
