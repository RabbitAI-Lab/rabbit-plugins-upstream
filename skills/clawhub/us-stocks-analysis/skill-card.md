## Description:

US Stocks Analysis helps agents produce read-only US equity research by combining SentiSense market data, public SEC and FRED evidence, quick workflows, and an adversarial investment-committee process with sourced disagreements and verdicts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide agents through educational US stock research, ticker due diligence, thesis red-teaming, and concise market-data briefs. The skill is designed for informational analysis only, not investment advice or trading execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key and can run the pinned sentisense npm CLI.

Mitigation: Provide the API key only in the intended environment, keep it out of transcripts and logs, and run the documented pinned CLI version from a trusted runtime.

Risk: Stock-analysis output could be mistaken for personalized financial advice.

Mitigation: Keep the educational disclaimer visible, avoid buy or sell instructions, and require every material claim to trace to an evidence ledger row or be marked unavailable.

Risk: Public-source fetching for SEC, FRED, or investor-relations evidence can expand network exposure if implemented too broadly.

Mitigation: Use the skill's narrow fetch-safety posture: fixed public hosts, public HTTP or HTTPS only, private-address blocking, redirect rechecks, response and time caps, and SEC user-agent/rate-limit discipline.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/us-stocks-analysis)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense application](https://app.sentisense.ai)
- [SEC company tickers reference](https://www.sec.gov/files/company_tickers.json)
- [SEC XBRL company concept endpoint](https://data.sec.gov/api/xbrl/companyconcept/CIK{10digits}/us-gaap/{Concept}.json)
- [FRED DGS10 CSV reference](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown analysis with sourced evidence ledger rows, concise verdicts, and optional shell or HTTP command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; requires SENTISENSE_API_KEY for SentiSense endpoints; no trading, purchases, wallet access, or write operations.]

## Skill Version(s):

2.6.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
