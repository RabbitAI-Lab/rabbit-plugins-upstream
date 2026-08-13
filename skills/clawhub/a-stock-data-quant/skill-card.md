## Description:

A-share stock quantitative analysis toolkit with 20+ technical indicators, 7 backtesting strategies, candlestick pattern recognition, multi-source data fallback, real-time quotes, AI financial analysis, news, chip distribution, board fund flow, F10 finance, research reports, and interactive answers.

This skill is for research and development only.

## Publisher:

[jangviktor-web](https://clawhub.ai/user/jangviktor-web)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to run A-share market analysis, technical indicators, backtests, stock comparisons, real-time quote lookups, financial data queries, and AI-assisted finance summaries. Its outputs are for learning and research and should not be treated as investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts multiple third-party finance and AI services.

Mitigation: Review the configured services and run it only in an environment where those network requests are acceptable.

Risk: The package ships obfuscated default API keys in config.yaml.

Mitigation: Replace or remove bundled defaults before use and prefer environment variables for your own service credentials.

Risk: Financial analysis output can be mistaken for investment advice.

Mitigation: Treat generated analysis as informational, verify source data, and keep the skill's investment-advice disclaimer visible in downstream use.

Risk: Unpinned dependencies and live market-data providers can change behavior over time.

Mitigation: Use an audited environment with pinned dependencies and test critical commands before relying on results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jangviktor-web/skills/a-stock-data-quant)
- [README](README.md)
- [AkShare](https://github.com/akfamily/akshare)
- [MyTT](https://github.com/mpquant/MyTT)
- [PanWatch](https://github.com/TNT-Likely/PanWatch)
- [Eastmoney Miaoxiang AI](https://ai.eastmoney.com/mxClaw)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, HTML files, shell commands, configuration, guidance]

**Output Format:** [Markdown or terminal text with optional JSON and generated HTML chart files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include market data tables, calculated indicators, backtest summaries, command examples, and finance-risk disclaimers.]

## Skill Version(s):

0.1.2 (source: server release metadata; artifact frontmatter reports 3.6.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
