## Description:

亚马逊商品利润核算专家。适用于核算 FBA 费用、头程到岸成本、佣金、仓储或弃置费用、广告假设、退货率影响、净利润、利润率、ROI 和商品盈利对比的场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon marketplace sellers and ecommerce operators use this skill to calculate ASIN-level profitability before product selection or sourcing decisions. It combines marketplace, sourcing, fee, advertising, return-rate, and storage assumptions into net profit, margin, ROI, and comparative HTML reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the bundle includes broad account, payment, upload, scheduling, catalog-write, memory, and telemetry capabilities.

Mitigation: Review enabled LinkFox capabilities before installation and confirm any upload, scheduled task, product-center write, payment or order action, or remembered parameter before use.

Risk: The security guidance says ASINs, product images, keywords, reports, account or onboarding data, and API keys may be sent to LinkFox services or saved locally.

Mitigation: Install only when LinkFox is trusted with marketplace research data and credentials, and avoid submitting sensitive data that is not needed for the profitability task.

Risk: Endpoint override environment variables can redirect LinkFox traffic.

Mitigation: Do not set LinkFox endpoint override environment variables unless the destination is controlled and trusted.

Risk: Profit estimates depend on external marketplace, sourcing, return-rate, advertising, exchange-rate, and FBA fee data that may be incomplete or stale.

Mitigation: Review report data-source notes, confirm supplier pricing and logistics assumptions, and rerun calculations with verified parameters before making commercial decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-profit-calculation-expert)
- [Workflow](artifact/skills/profit-calculation-expert/references/workflow.md)
- [Data fields](artifact/skills/profit-calculation-expert/references/data-fields.md)
- [Output schema](artifact/skills/profit-calculation-expert/references/output-schema.md)
- [FBA fee table](artifact/skills/profit-calculation-expert/references/fba-fee-table.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Concise text or Markdown summary with an HTML report path; intermediate profit data is structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ASIN input; reports include cost breakdowns, supplier matches, profit metrics, and data-source notes]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
