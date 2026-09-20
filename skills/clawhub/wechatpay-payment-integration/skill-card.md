## Description:

Provides WeChat Pay integration support for product selection, official examples, integration quality checks, Q&A, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencent-adm](https://clawhub.ai/user/tencent-adm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and merchant support teams use this skill to plan, implement, review, and troubleshoot Mainland China WeChat Pay integrations using official documentation and local helper workflows.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill can silently make outbound connections and self-update from a remote bundle.

Mitigation: Install and run it only in an approved environment, and prefer a versioned, signed, reviewable update process before accepting remote updates.

Risk: Live troubleshooting workflows may involve Authorization headers, signatures, P12 certificates, and merchant identifiers.

Mitigation: Treat these values as sensitive, redact where possible, use test credentials when feasible, and paste live secrets into chat only when organizational policy permits it.

Risk: The skill may require npm CLI installation and local helper scripts.

Mitigation: Review helper scripts and install CLI dependencies through controlled package-management channels before deployment.

## Reference(s):

- [Skill page](https://clawhub.ai/tencent-adm/skills/wechatpay-payment-integration)
- [Publisher profile](https://clawhub.ai/user/tencent-adm)
- [基础概念及业务介绍](references/基础概念及业务介绍.md)
- [文档检索与问答](references/文档检索与问答.md)
- [wechatpay-dev-cli 使用说明](references/wechatpay-dev-cli使用说明.md)
- [APIv3 接口动态排障](references/APIv3接口动态排障.md)
- [接入质量检查清单](references/接入质量检查清单.md)
- [如何理解用户问题](references/如何理解用户问题.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions, API Calls]

**Output Format:** [Markdown with inline code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include official-documentation citations, troubleshooting steps, quality review findings, and helper-command proposals.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
