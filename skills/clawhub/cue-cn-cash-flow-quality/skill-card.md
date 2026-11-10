## Description:

把经营、投资、筹资现金流、相关比率及间接法调节表整理成逐项附原句、定位锚点和来源编号的现金流质量记录。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT

## Use Case:

财务分析人员可用它把财报中的经营、投资、筹资现金流及相关比率整理为带原文依据的登记稿，并逐项核对净利润调节表。它只记录披露事实，不判断造假，也不提供预测或评级。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security guidance notes that optional MCP discovery does not clearly match the financial-analysis purpose.

Mitigation: Before configuring CUE_API_KEY, review the catalog and routing destination and confirm the available tools are appropriate; use the documented zero-channel workflow otherwise.

Risk: Security guidance reports partial scanner coverage and a weakness in evidence checks.

Mitigation: Manually verify source quotes and anchors in the resulting register instead of relying on automated validation alone.

## Reference(s):

- [ClawHub release](https://clawhub.ai/huhoo/skills/cue-cn-cash-flow-quality)
- [Optional MCP tool catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Markdown, Analysis]

**Output Format:** [Markdown cash-flow fact register with source quotes and anchors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each figure is tied to a source ID; self-computed ratios must identify their numerator and denominator sources.]

## Skill Version(s):

0.1.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
