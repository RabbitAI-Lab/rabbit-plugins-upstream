## Description:

左侧定投决策计算器。输入当前指数点位、近一年最高点、持仓成本、汇率，输出是否触发定投、加仓倍数、换汇建议、风险提示。

This skill is ready for commercial/non-commercial use.

## Publisher:

[987618350-cmd](https://clawhub.ai/user/987618350-cmd)

### License/Terms of Use:

MIT

## Use Case:

External users use this skill to calculate DCA trigger status, position sizing, currency-exchange considerations, and holding diagnostics from user-supplied index, cost, funds, and exchange-rate data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad finance triggers may activate investment, exchange, holding, or reduction guidance outside a clearly requested calculation workflow.

Mitigation: Install and use the skill only when that finance workflow is intended, require explicit user-supplied data before calculations, and independently verify calculations and recommendations.

Risk: Generated DCA and exchange outputs can be advice-like and may be mistaken for personalized financial advice.

Mitigation: Keep outputs framed as calculation support, preserve the skill requirement to avoid price or exchange-rate prediction, and include market, currency, and liquidity risk warnings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/987618350-cmd/skills/nvc-communication-guide)
- [987618350-cmd publisher profile](https://clawhub.ai/user/987618350-cmd)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with structured calculation reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided financial inputs and includes risk warnings in generated reports.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
