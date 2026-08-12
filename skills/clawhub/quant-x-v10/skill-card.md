## Description:

QUANT-X v10 is an A-share quantitative strategy dashboard for monitoring 600330 with Tencent market data, multi-factor scoring, order-book imbalance views, sector comparison, large-order tiers, technical levels, and trading-style signal summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[43906351-debug](https://clawhub.ai/user/43906351-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect a browser-based A-share market dashboard, review simplified quantitative indicators, and prepare local or static-web deployment steps. It is best treated as informational market-analysis support rather than authoritative investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat simplified score labels and buy/sell-style actions as rigorous financial advice.

Mitigation: Present the dashboard as informational analysis only and require independent review before acting on position-sizing or trading recommendations.

Risk: The dashboard sends watched stock symbols to Tencent market-data services every 3 seconds.

Mitigation: Disclose the external market-data polling behavior before deployment and use it only where that network sharing is acceptable.

Risk: The dashboard loads Chart.js from an external CDN.

Mitigation: Review the dependency source for the deployment environment or pin and host the approved library internally.

Risk: Displayed quantitative methods are based on simplified heuristics rather than full technical indicators or verified backtests.

Mitigation: Label generated signals as heuristic summaries and validate calculations against an approved financial-analysis workflow before operational use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/43906351-debug/skills/quant-x-v10)
- [Publisher Profile](https://clawhub.ai/user/43906351-debug)
- [Scoring Formula Reference](artifact/references/scoring-formula.md)
- [Deployment Workflow](artifact/workflows/deploy.md)
- [Tencent Quote Endpoint](https://qt.gtimg.cn/q=sh600330)
- [Tencent K-Line Endpoint](https://web.ifzq.gtimg.cn/appstock/app/fqkline/get)
- [Tencent Minute Data Endpoint](https://web.ifzq.gtimg.cn/appstock/app/minute/query)
- [Chart.js Distribution](https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and a static HTML dashboard artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Browser dashboard polls Tencent market-data services and renders Chart.js visualizations.]

## Skill Version(s):

1.0.0 (source: server release metadata, artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
