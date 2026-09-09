## Description:

Fetches Chinese financial-market data and investment research information across A-shares, Hong Kong stocks, funds, indices, financials, announcements, research reports, and macroeconomic datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find, fetch, compare, and export structured Chinese financial-market and research datasets for analysis. It is not intended for direct trading advice, automated order execution, or conclusions that require inventing missing data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed if supplied directly in command-line arguments during non-interactive initialization.

Mitigation: Prefer interactive initialization and avoid placing real API keys in shell history, logs, scripts, or shared terminals.

Risk: Auto-update or skipped verification can increase supply-chain risk if the update source is not trusted.

Mitigation: Do not enable auto-update or skip verification unless the update source and operational risk are understood.

Risk: Financial data, signals, and analysis can be mistaken for personalized investment advice.

Mitigation: Treat returned data as research input, state data limits clearly, and avoid direct buy, sell, or order-execution recommendations.

Risk: Empty, unavailable, permission-limited, or network-limited results may lead to unsupported conclusions.

Mitigation: Report the query scope or access limitation and stop any inference that depends on missing data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [English API reference index](artifact/docs/references-index.en.md)
- [Market data reference](artifact/references/市场数据.md)
- [Base data reference](artifact/references/基础数据.md)
- [Bond data reference](artifact/references/债券.md)
- [Large model corpus reference](artifact/references/大模型语料.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and structured data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference InvestToday CLI endpoints, query parameters, examples, and returned financial data fields.]

## Skill Version(s):

1.8.82 (source: server release metadata, released 2026-09-08T14:52:48Z)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
