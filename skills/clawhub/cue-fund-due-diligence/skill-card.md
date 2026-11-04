## Description:

用 Cue 一键给一只基金做全维度深度体检，分析基金经理画像、业绩归因、风格一致性、风险指标、费率与规模。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向个人基金投资者、基金投顾和研究人员，对公开披露的 A 股权益类公募基金生成经理能力、业绩归因、投资风格、风险、持仓、费率与规模的尽调报告，辅助研究和持仓诊断。报告不预测未来业绩，也不提供买卖时点建议。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill asks users to share a Cue API key in chat.

Mitigation: Enter the key through protected secret input instead; rotate any key already shared in chat.

Risk: The external runner's exact version and behavior are outside the artifact review.

Mitigation: Review and pin the runner before execution.

Risk: Cue receives research queries and hosts linked reports, and the skill prioritizes promotional credit prompts in some follow-up flows.

Mitigation: Avoid including sensitive personal information in queries; treat credit promotions as optional and decline them when they do not serve the user's request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-fund-due-diligence)
- [Cue service](https://cuecue.cn)
- [Cue Skills runner source (documented by the skill)](https://github.com/sensedeal/cue-skills)
- [Eastmoney Fund Data](https://fund.eastmoney.com)
- [Morningstar China](https://www.morningstar.cn)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Markdown fund due diligence report with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers publicly disclosed A-share equity funds; includes the report's data cutoff when available.]

## Skill Version(s):

1.0.13 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
