## Description: <br>
US stocks analysis by an adversarial investment committee that combines quick data workflows with sourced sentiment, smart-money, SEC fundamentals, and reconciled investor-persona verdicts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesentitrader](https://clawhub.ai/user/thesentitrader) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and analysts use this skill to produce educational US-equity briefs or thesis-grade committee analysis with sourced evidence ledgers, adversarial persona review, and recorded dissents. It is read-only and does not trade, purchase securities, modify accounts, or access wallets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ticker or query metadata and API-key authenticated requests are sent to SentiSense and public financial-data sources. <br>
Mitigation: Use only when comfortable sharing that metadata, protect SENTISENSE_API_KEY, and avoid entering brokerage credentials or personal financial details. <br>
Risk: Outputs could be mistaken for investment advice or personalized recommendations. <br>
Mitigation: Treat results as educational analysis, verify sourced figures, and make independent decisions; the skill does not trade or modify accounts. <br>
Risk: Market data, public filings, or sentiment samples may be unavailable, stale, or thinly sampled. <br>
Mitigation: Use the skill's as-of dates, thin-sample guards, NOT AVAILABLE markers, and confidence caps instead of filling gaps with guesses. <br>


## Reference(s): <br>
- [ClawHub Skill: us-stocks-analysis](https://clawhub.ai/thesentitrader/skills/us-stocks-analysis) <br>
- [SentiSense Website](https://sentisense.ai) <br>
- [SentiSense API Reference](https://sentisense.ai/skill.md) <br>
- [SentiSense API Key Setup](https://app.sentisense.ai/get-api-key) <br>
- [SEC Company Tickers](https://www.sec.gov/files/company_tickers.json) <br>
- [FRED DGS10 CSV](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, guidance] <br>
**Output Format:** [Markdown analysis with evidence ledgers, quick-read briefs, committee verdicts, and optional shell commands for bounded API calls.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for SentiSense endpoints; public SEC EDGAR and FRED fetches are bounded when available.] <br>

## Skill Version(s): <br>
2.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
