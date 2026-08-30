## Description:

一次付费通过 VIN 生成车辆配置档案、登记五项、过户流转和车检估算摘要的购前车辆尽调报告，并在付款前要求用户确认车辆类型与事故/非法改装情况。

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to run paid pre-purchase vehicle due diligence from a VIN when they need configuration, registration, ownership-transfer history, and inspection-estimate information in one Markdown report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow shares VIN and vehicle-query details with Juhe and uses an Alipay payment flow.

Mitigation: Confirm user consent, payment amount, vehicle type, and accident/illegal-modification status before sending the paid query.

Risk: Vehicle reports may be mistaken for complete accident, theft, lien, valuation, or purchase-decision advice.

Mitigation: Present the report as limited due-diligence information, avoid buy/sell recommendations, and keep disclaimers visible.

Risk: Returned plate data or query details could expose sensitive vehicle information if displayed or logged verbatim.

Mitigation: Mask license plates in all outputs and avoid storing full VIN, vehicle type, accident status, or raw query text in logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-vehicle-dd-pro-a2a)
- [Juhe A2A query endpoint](https://apis.juhe.cn/a2a/query)
- [README.md](artifact/README.md)
- [PRODUCT.md](artifact/PRODUCT.md)
- [OUT_FORMAT.md](artifact/OUT_FORMAT.md)

## Skill Output:

**Output Type(s):** [Markdown, API Calls, Guidance]

**Output Format:** [Markdown report with structured tables and concise guidance after a paid API workflow]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user consent, valid VIN, vehicle type, accident/illegal-modification status, Alipay payment confirmation, and masked license-plate display.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
