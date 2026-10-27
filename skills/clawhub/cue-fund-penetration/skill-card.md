## Description:

用 Cue 穿透你的基金组合持仓——你以为分散了，其实买了一篮子同样的东西。逐层拆解股票/行业/风格暴露，检测重复配置与集中度风险，逐只排雷。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向持有多只 A 股公募基金的投资者，用于穿透已披露的前十大持仓，识别个股重复、行业集中与风格偏向，并形成组合诊断和调仓方向建议；不提供实时持仓或未来业绩预测。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The downloaded runner recommends disabling sandbox protections when network connections fail.

Mitigation: Review and pin the runner before installation; keep sandbox protections enabled and investigate the connection issue without disabling them.

Risk: Portfolio queries are sent to Cue and research runs consume Cue credits.

Mitigation: Configure the API key locally rather than pasting it into chat, and confirm the portfolio information and credit use are acceptable before running a query.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-fund-penetration)
- [Cue](https://cuecue.cn/)
- [Eastmoney Fund](https://fund.eastmoney.com)
- [Morningstar China](https://www.morningstar.cn)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [中文结构化 Markdown 诊断报告，包含组合概览、基金持仓穿透、个股重叠、行业集中度、风格暴露、风险评级及调仓方向建议。]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [基于已披露持仓，通常为基金前十大重仓股；非实时持仓或未来业绩预测。]

## Skill Version(s):

1.0.11 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
