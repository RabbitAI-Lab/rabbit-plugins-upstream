## Description:

Sentiment and smart-money positioning for US stocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve SentiSense market sentiment, smart-money positioning, AI insights, and sentiment-tagged news for US equities. The skill supports educational market context and does not provide personalized trading advice or order-entry capability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a SentiSense API key.

Mitigation: Store SENTISENSE_API_KEY in the environment, do not put it in URLs or user-facing output, and install only when API-key access to SentiSense is acceptable.

Risk: Market sentiment and smart-money outputs could be mistaken for financial advice.

Mitigation: Present outputs as educational market context and avoid personalized buy, sell, portfolio, or order-entry recommendations.

Risk: API quota or rate limits may affect use on free or paid plans.

Mitigation: Watch request volume and back off when the API returns rate-limit responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-sentiment)
- [Publisher profile](https://clawhub.ai/user/thesentitrader)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense skill API reference](https://sentisense.ai/skill.md)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with optional JSON summaries, shell commands, or Python command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY and network access to the SentiSense API; outputs are informational market context, not financial advice.]

## Skill Version(s):

0.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
