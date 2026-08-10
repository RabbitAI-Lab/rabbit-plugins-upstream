## Description:

春登台V3·A股短线精灵。触发：分析/诊断/选股A股。核心：腾讯实时行情+V3量化评分+三维定性框架+双卖出规则+仓位风控，适用隔日超短与主升浪两种模式。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jinxulin8899-dotcom](https://clawhub.ai/user/jinxulin8899-dotcom)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill to analyze or diagnose A-share stocks with Tencent quote data, a V3 scoring model, qualitative factors, sell rules, and position sizing guidance. Outputs should be treated as informational trading analysis, not personalized financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can produce confident buy, sell, and position guidance for A-share trading.

Mitigation: Treat outputs as informational analysis only and require users to verify market data and decisions independently.

Risk: The skill promotes private signal access and strategy contact channels.

Mitigation: Review the contact and signal-promotion content before installation and do not treat it as validated investment advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jinxulin8899-dotcom/skills/chundengtai-v3)
- [Tencent real-time quote endpoint](https://qt.gtimg.cn/q=sh600143)
- [Tencent historical K-line endpoint](https://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param=sh600143,day,,,60,qfq)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Plain text with bracketed key facts, pipe-separated tables, and a data freshness marker]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected to append a quality-control marker and avoid Markdown symbols in user-facing analysis.]

## Skill Version(s):

1.0.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
