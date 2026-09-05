## Description:

US Stocks Analysis guides agents through read-only US equity research by combining quick data workflows with an adversarial investment committee that records sourced evidence, disagreements, and verdicts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to produce sourced US stock research briefs and thesis reviews for tickers, including price, sentiment, smart-money, analyst, SEC, and macro evidence. The workflow is informational and read-only, with no trading, purchase, write, or wallet-access capabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user could mistake the generated stock research for personalized investment advice.

Mitigation: Keep the skill's informational-only and not-investment-advice framing in outputs, and require users to make their own decisions.

Risk: The workflow uses a SentiSense API key and makes external financial-data requests.

Mitigation: Install only after trusting the SentiSense service and npm CLI package, and provide the API key through the documented environment variable.

Risk: Incorrect ticker resolution or stale external data can produce misleading research.

Mitigation: Resolve company names before fetching, source every number in the evidence ledger, and mark unavailable data instead of guessing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/us-stocks-analysis)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API base URL](https://app.sentisense.ai)
- [SEC company ticker reference](https://www.sec.gov/files/company_tickers.json)
- [SEC XBRL company concept API](https://data.sec.gov/api/xbrl/companyconcept/CIK{10digits}/us-gaap/{Concept}.json)
- [FRED 10-year Treasury CSV](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, API calls, Guidance]

**Output Format:** [Markdown with sourced evidence tables, verdict templates, and inline shell or API command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for SentiSense calls; outputs are read-only and informational, not investment advice or trading instructions.]

## Skill Version(s):

2.7.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
