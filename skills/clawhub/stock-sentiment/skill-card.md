## Description:

Sentiment and smart-money positioning for US stocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and research agents use this skill to review US-stock sentiment, market mood, news, and insider, congressional, institutional, and analyst activity as educational market context rather than investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposure of the SentiSense API key in prompts or shared logs.

Mitigation: Keep SENTISENSE_API_KEY in the environment, avoid printing it, and allow read-only HTTPS requests only to app.sentisense.ai.

Risk: Treating sentiment or delayed market data as personalized investment advice or real-time prices.

Mitigation: Present outputs as educational context, identify data age and preview limitations, and avoid buy or sell recommendations.

## Reference(s):

- [ClawHub release](https://clawhub.ai/thesentitrader/skills/stock-sentiment)
- [SentiSense API skill reference](https://sentisense.ai/skill.md)
- [SentiSense website](https://sentisense.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown prose with dated market-data observations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a SentiSense API key; free-tier responses may be preview-limited and supporting prices may be delayed.]

## Skill Version(s):

0.5.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
