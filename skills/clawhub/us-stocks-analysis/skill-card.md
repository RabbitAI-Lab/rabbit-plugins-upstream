## Description:

US Stocks Analysis provides read-only US equities research workflows, including quick market briefs and an adversarial investment-committee process that grounds stock theses in sourced evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent users can use this skill to structure educational stock research, due diligence on US tickers, bull-versus-bear analysis, and sourced committee-style investment thesis reviews. The skill is informational only and does not place trades, make purchases, access wallets, or provide personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stock tickers and related research queries may be sent to SentiSense during normal use.

Mitigation: Use the skill for educational research, keep SENTISENSE_API_KEY scoped to SentiSense, and disclose expected external data use before installation.

Risk: Financial analysis output could be mistaken for personalized investment advice or a trade recommendation.

Mitigation: Keep outputs informational, include the educational disclaimer, and avoid buy/sell instructions, allocation advice, trading actions, purchases, or wallet access.

Risk: Public SEC or FRED fetching can become overbroad if the host exposes general URL access.

Mitigation: Enforce the documented narrow fetch behavior for approved public sources and reject private, loopback, metadata, non-HTTP, oversized, or slow fetch targets.

Risk: Users may overstate freshness because price is delayed and sentiment, score, insights, mood, and options summaries are batch or end-of-day data.

Mitigation: Carry as-of timestamps, use priceAsOf where present, state that price is 15-minute delayed, and avoid describing outputs as real time.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/us-stocks-analysis)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API Terms of Service](https://sentisense.ai/agreement/API-Terms-of-Service.pdf)
- [SentiSense Terms of Service](https://sentisense.ai/agreement/Terms-of-Service.pdf)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis briefs, evidence ledgers, committee verdicts, and inline API or shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only stock research output; requires SENTISENSE_API_KEY for SentiSense endpoints; price data must be treated as 15-minute delayed and other data must carry as-of timestamps.]

## Skill Version(s):

2.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
