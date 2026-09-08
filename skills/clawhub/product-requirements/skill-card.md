## Description:

将 Amazon 评论痛点、商品字段和使用场景整理为可验证的产品需求与验收问题；仅用于需求整理，不用于研发排期承诺、采购执行或销量预测，并需要 ARI API key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon operators, product managers, and ecommerce teams use this skill to turn review pain points, product fields, and usage scenarios into verifiable product requirements and acceptance questions. It helps structure product-requirements analysis after checking ARI account access, product data, pricing, and explicit confirmation for paid operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key and can access account review data, balances, reports, alerts, exports, and monitoring settings.

Mitigation: Authorize only the intended ARI account, do not share the API key in prompts or reports, and revoke or rotate the key if access is no longer needed.

Risk: Some paid analyses may run under server-side auto-confirm behavior, which can consume credits without a fresh prompt for each small operation.

Mitigation: Set billing confirmation to always ask when predictable spend control is required, and review quoted credits and balance before confirming paid runs.

Risk: Schedules, watches, competitor tracking, and exports can broaden ongoing data collection or account activity beyond a single requirements report.

Mitigation: Enable monitoring, competitor relationships, exports, or schedule changes only after an explicit user request and after checking the returned account capability and cost details.

Risk: Requirements derived from review samples can be incomplete or misleading when product data, review count, or collection windows are limited.

Mitigation: State the data range, sample size, and known gaps, and avoid using the output as a delivery commitment, procurement instruction, sales forecast, or sole decision source.

## Reference(s):

- [Amazon 产品需求整理 README](README.md)
- [ARI CLI 与 API 参考](references/reference.md)
- [Amazon 产品需求整理 专属运营工作流](references/operation-workflow.md)
- [ARI API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI products](https://ari.funewa.com/zh/products)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with concise analysis, quoted ARI data, command guidance, and report links or exports when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ARI account authorization and may rely on server-side product, review, billing, report, alert, export, and monitoring data.]

## Skill Version(s):

1.4.8 (source: server release evidence, target metadata, artifact frontmatter, _meta.json, and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
