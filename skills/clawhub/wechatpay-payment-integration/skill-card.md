## Description:

微信支付（WeChat Pay）相关问题的统一入口，处理与微信支付接入、产品、开发、运营、品牌经营相关的咨询，提供产品选型、官方示例代码、接入质量评估、答疑与排障。

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencent-adm](https://clawhub.ai/user/tencent-adm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to answer WeChat Pay integration questions, choose payment products, retrieve official examples, review integration quality, and troubleshoot APIv3 payment issues.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill can run networked update code and refresh local resources from external endpoints.

Mitigation: Install only from a trusted publisher, review updates before use, and prefer signed or pinned resources where available.

Risk: The skill may install or use a global WeChat Pay CLI and send troubleshooting context to an external service.

Mitigation: Confirm the CLI package source and version, get user consent before networked troubleshooting, and avoid sending unnecessary business or payment data.

Risk: The skill handles WeChat Pay authorization and signature material during API troubleshooting.

Mitigation: Keep certificates, private keys, and signing material local; redact sensitive values from logs and chat; use least-privilege credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tencent-adm/skills/wechatpay-payment-integration)
- [基础概念及业务介绍](references/基础概念及业务介绍.md)
- [文档检索与问答](references/文档检索与问答.md)
- [wechatpay-dev-cli 使用说明](references/wechatpay-dev-cli使用说明.md)
- [APIv3 接口动态排障](references/APIv3接口动态排障.md)
- [微信支付接入质量检查清单（通用）](references/接入质量检查清单.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code blocks, shell commands, and structured troubleshooting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API troubleshooting commands and code-review findings; relies on official WeChat Pay documentation when available.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
