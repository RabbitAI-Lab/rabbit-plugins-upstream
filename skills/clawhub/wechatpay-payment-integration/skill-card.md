## Description:

Provides WeChat Pay integration guidance for product selection, official example-code lookup, integration quality review, Q&A, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencent-adm](https://clawhub.ai/user/tencent-adm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and integration engineers use this skill to choose WeChat Pay products, retrieve official API examples, review implementation quality, and troubleshoot APIv2/APIv3 integration issues for merchants.

### Deployment Geography for Use:

China (mainland merchants)

## Known Risks and Mitigations:

Risk: The skill can update and replace local skill files from Tencent-hosted archives.

Mitigation: Review update behavior before use and run synchronization only in a controlled workspace where file replacement is acceptable.

Risk: The skill may install or upgrade a global npm CLI and contact external WeChat Pay CLI or backend services.

Mitigation: Confirm network, package-management, and external-service use before enabling the workflows in sensitive environments.

Risk: Troubleshooting workflows can involve payment context, authorization headers, certificates, signatures, keys, or customer and transaction data.

Mitigation: Do not share private keys, certificates, full Authorization headers, customer data, or production transaction details unless the flow has been reviewed and intentionally approved.

## Reference(s):

- [APIv3接口动态排障](references/APIv3接口动态排障.md)
- [wechatpay-dev-cli使用说明](references/wechatpay-dev-cli使用说明.md)
- [基础概念及业务介绍](references/基础概念及业务介绍.md)
- [如何理解用户问题](references/如何理解用户问题.md)
- [接入质量检查清单](references/接入质量检查清单.md)
- [文档检索与问答](references/文档检索与问答.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code blocks and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CLI commands, API request guidance, code-review findings, and cited reference paths.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
