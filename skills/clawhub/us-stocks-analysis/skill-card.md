## Description:

US Stocks Analysis helps agents produce read-only, evidence-led US equity research using SentiSense data, SEC/FRED sources, quick workflows, and an adversarial investment-committee process.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run read-only US stock research, quick market data briefs, and structured adversarial thesis reviews. It is intended for educational analysis, due diligence support, and evidence-grounded discussion, not personalized investment advice or trade execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outputs could be mistaken for personalized investment advice or trading instructions.

Mitigation: Keep outputs framed as educational analysis, avoid personalized recommendations, and do not provide trade execution, allocation, or account-changing instructions.

Risk: Ticker research requests are sent to SentiSense using an API key and may use public SEC/FRED data.

Mitigation: Store the API key in SENTISENSE_API_KEY, avoid exposing credentials in prompts or logs, and follow the skill's fetch safety and rate-limit guidance.

Risk: Financial conclusions can be misleading when source data is stale, missing, or unavailable.

Mitigation: Use the evidence ledger, mark missing data as NOT AVAILABLE, cite source rows, and lower confidence when key evidence is incomplete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/us-stocks-analysis)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SEC company tickers reference](https://www.sec.gov/files/company_tickers.json)
- [FRED DGS10 CSV reference](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with structured tables, checklists, and inline shell or HTTP commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only analysis; SentiSense data requests require SENTISENSE_API_KEY.]

## Skill Version(s):

2.6.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
