## Description:

Searches financial markets, securities, public company fundamentals, prices, K-line data, filings, financial news, A-share data, Hong Kong stocks, and global tickers using yfinance, mootdx, API scripts, or browser-use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve and cross-check market data, issuer fundamentals, filings, financial statements, and finance news across global and China-focused sources. It helps produce sourced market research outputs while keeping ticker, market, time range, metric definitions, and source URLs visible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Finance libraries make outbound requests to market-data and news providers, which can reveal queried tickers or depend on third-party availability.

Mitigation: Use the skill only in approved network contexts, retain source URLs, and cross-check important facts against public pages or official disclosures.

Risk: The tdx-affair-fetch command downloads user-selected financial data files to disk.

Mitigation: Set an intended download directory, inspect downloaded files before parsing, and avoid writing into sensitive or shared paths.

Risk: Market data, news, and financial fields may be delayed, incomplete, or unsuitable as investment advice.

Mitigation: Report the market, ticker, time range, metric basis, and source for each result, and do not present script output as investment advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-search-finance)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON command output from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve ticker or security code, market, time range, metric basis, and source URL; script commands emit JSON.]

## Skill Version(s):

2026.8.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
