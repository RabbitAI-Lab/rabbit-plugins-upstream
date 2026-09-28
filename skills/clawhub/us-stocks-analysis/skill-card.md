## Description:

Provides read-only US stock research through quick data briefs and an evidence-based investment committee that tests competing theses and presents a plain-English verdict.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, analysts, and other users can research US stocks, compare bull and bear cases, and review sourced evidence and unresolved disagreements. The output is educational analysis, not personalized investment advice or a trading instruction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stock research queries and an API credential are sent to SentiSense.

Mitigation: Review the data-sharing implications before use and provide the SentiSense API key through the environment rather than in a prompt.

Risk: Educational analysis or delayed market data may be mistaken for current, personalized investment advice.

Mitigation: Check as-of timestamps and primary evidence, and make independent investment decisions; the skill cannot place trades.

## Reference(s):

- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)
- [US Stocks Analysis on ClawHub](https://clawhub.ai/thesentitrader/skills/us-stocks-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Plain-English Markdown briefs and sourced investment-committee verdicts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cites an evidence ledger and labels delayed price data; no trades or account actions.]

## Skill Version(s):

2.9.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
