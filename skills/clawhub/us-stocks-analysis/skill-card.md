## Description:

US Stocks Analysis helps agents produce educational US-equity briefs and adversarial investment-committee analyses using SentiSense read-only market data, sourced evidence ledgers, and recorded bull/bear disagreements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill for educational US-stock research, quick market-data briefs, investment-thesis due diligence, and structured bull-versus-bear analysis. It is designed to keep numerical claims tied to an evidence ledger and to avoid trading, purchasing, or write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stock queries and the API key are used with SentiSense.

Mitigation: Review the SentiSense terms and configure the SENTISENSE_API_KEY only for intended use; the skill declares read-only access to app.sentisense.ai.

Risk: Users could mistake committee verdicts or quick reads for personalized buy or sell instructions.

Mitigation: Keep the educational, non-advisory framing visible and treat outputs as research inputs rather than trading recommendations.

Risk: Preview limits, quotas, delayed prices, or batch-generated signals can affect completeness and freshness.

Mitigation: Carry source rows, as-of timestamps, and any preview or quota limitations into the final analysis before drawing conclusions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/thesentitrader/skills/us-stocks-analysis)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense website](https://sentisense.ai)
- [SentiSense application](https://app.sentisense.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis with sourced evidence summaries and optional curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; read-only network access is scoped to app.sentisense.ai; outputs are educational market research, not financial advice.]

## Skill Version(s):

2.7.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
