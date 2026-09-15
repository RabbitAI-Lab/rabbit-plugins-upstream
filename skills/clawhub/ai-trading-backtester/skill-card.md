## Description:

Designs, implements, and evaluates Python trading strategy backtests across A-share, Hong Kong, and US equity markets.

This skill is for research and development only.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

External quantitative analysts, developers, and retail traders use this skill to turn trading ideas into Python backtests, compare strategy behavior, and produce risk-adjusted performance reports. It is an educational and research-oriented assistant, not a live trading or financial advice system.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated strategy code or data-source choices may be incorrect, incomplete, or unsuitable for a real environment.

Mitigation: Review generated code and data sources before running any backtest, and validate assumptions such as costs, slippage, liquidity, suspensions, and market-specific trading rules.

Risk: Backtest outputs may be mistaken for investment advice or live trading instructions.

Mitigation: Treat outputs as educational research only; do not connect them to brokerage accounts or trade on them without separate controls and qualified professional review.

Risk: Historical results can be misleading because of overfitting, future-looking data, survivorship bias, or unmodeled execution constraints.

Mitigation: Use out-of-sample and walk-forward testing, include realistic transaction costs and slippage, and compare stress scenarios before relying on results.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with Python and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include illustrative performance tables, strategy templates, and risk-control guidance; outputs are not financial advice.]

## Skill Version(s):

5.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
