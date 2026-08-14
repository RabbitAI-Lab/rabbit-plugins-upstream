## Description:

Analyze Chinese stock prices (A-shares, HK stocks) and provide investment recommendations. Use when the user asks about stock analysis for Chinese companies, including buying/selling recommendations and market trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze current prices, market context, and technical signals for Chinese A-share, Hong Kong, and related US-listed stocks. It supports structured stock analysis with buy, hold, or sell recommendations and risk disclaimers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stock recommendations may be incorrect, incomplete, or outdated because they depend on public market data and news available at response time.

Mitigation: Verify prices, news, and financial assumptions against current market sources before acting.

Risk: Users may over-rely on generated buy, hold, or sell guidance for financial decisions.

Mitigation: Treat outputs as informational analysis only and seek appropriate professional advice for investment decisions.

## Reference(s):

- [Popular Chinese Stocks Reference](references/china-stocks.md)
- [Eastmoney](https://www.eastmoney.com)
- [Xueqiu](https://xueqiu.com)
- [Yahoo Finance](https://finance.yahoo.com)
- [Google Finance](https://www.google.com/finance)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Structured Markdown with tables, technical analysis, recommendation rationale, and risk disclaimer]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May rely on current public market data and news gathered at response time.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
