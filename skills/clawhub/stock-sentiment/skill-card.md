## Description:

Provides read-only sentiment, market-mood, news, and investor-positioning context for US stocks through SentiSense.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and analysts use this skill to review US-stock sentiment, market mood, and insider, congressional, institutional, and analyst activity as informational context, not personalized investment advice.

### Deployment Geography for Use:

Global (US equities coverage)

## Known Risks and Mitigations:

Risk: The skill sends a SentiSense API key to SentiSense for data requests.

Mitigation: Use a dedicated API key and provide it only to the intended SentiSense service.

Risk: Financial sentiment could be mistaken for investment advice or a trading instruction.

Mitigation: Present results as educational context, not personalized buy or sell recommendations.

Risk: Batch data and limited previews can obscure recency or omit relevant activity.

Mitigation: State data timestamps and label partial previews without inferring absence from a slice.

## Reference(s):

- [ClawHub stock-sentiment release](https://clawhub.ai/thesentitrader/skills/stock-sentiment)
- [SentiSense API skill documentation](https://sentisense.ai/skill.md)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Analysis]

**Output Format:** [Plain text or Markdown summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dated market signals; free-tier results may be partial previews.]

## Skill Version(s):

0.6.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
