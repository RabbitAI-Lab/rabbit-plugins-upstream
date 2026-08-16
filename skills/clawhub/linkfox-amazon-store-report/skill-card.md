## Description:

亚马逊店铺报告自动化获取技能，支持库存报告、订单报告、销售流量报告、FBA报告、财务结算报告等95+种报告类型的请求、轮询、下载和解压。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, marketplace operators, and their agents use this skill to retrieve structured Amazon Seller and Vendor reports, including inventory, orders, sales, traffic, FBA, returns, financial settlement, and Brand Analytics reports. The skill depends on a separate authorization skill for store selection and token management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can download sensitive Amazon seller report data and persist report metadata or files locally.

Mitigation: Review where files and metadata are stored, restrict access to the workspace, and remove downloaded reports when they are no longer needed.

Risk: The skill can expose downloaded report files through short-lived localhost URLs.

Mitigation: Disable local HTTP serving for sensitive reports when possible and avoid sharing generated URLs.

Risk: The skill includes account, billing, payment, and feedback-reporting flows in addition to report retrieval.

Mitigation: Confirm any purchase, order, or account action explicitly before continuing, and install only in environments where those flows are acceptable.

Risk: The skill requires API keys and access to LinkFox and Amazon report APIs.

Mitigation: Confirm where API keys are configured, limit credential exposure, and use the separate authorization dependency for store and token management.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-report)
- [Developer Proxy API Reference](artifact/references/api.md)
- [Onboarding and Account Guidance](artifact/references/onboarding.md)
- [Supported Report Types](artifact/references/report-types.md)
- [Amazon SP-API Report Type Values](https://developer-docs.amazon.com/sp-api/docs/report-type-values)
- [Amazon Selling Partner API Report Schemas](https://github.com/amzn/selling-partner-api-models/tree/main/schemas/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, shell commands, JSON responses, local report files, and short-lived localhost download URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report outputs can include local file paths, file URIs, extracted-file HTTP URLs, report identifiers, document identifiers, compression metadata, temporary directory paths, and file sizes.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
