## Description:

Sentiment and smart-money positioning for US stocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query SentiSense read-only market sentiment, smart-money positioning, analyst activity, AI insights, news, and market mood for US equities. The skill supports educational market context and synthesis, not order entry, portfolio management, or personalized financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to SENTISENSE_API_KEY.

Mitigation: Keep the key in the environment, send it only in the X-SentiSense-API-Key header, and do not place it in URLs or user-facing output.

Risk: The skill makes outbound requests to app.sentisense.ai.

Mitigation: Allow network access only to the documented SentiSense API host and prefer the bundled read-only Python helper or curl for narrow behavior.

Risk: Market sentiment outputs could be mistaken for personalized investment advice.

Mitigation: Frame responses as educational context, avoid buy or sell recommendations, and do not support order entry, wallet actions, or portfolio management.

Risk: Preview, rate-limit, or delayed data can make market context incomplete or stale.

Mitigation: Surface preview and freshness indicators, honor Retry-After on 429 responses, and distinguish sentiment metrics from delayed price data.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API Skill Reference](https://sentisense.ai/skill.md)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [SentiSense API Base](https://app.sentisense.ai)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/stock-sentiment)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown prose with optional JSON summaries and inline shell or Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should cite fresh API results, preserve preview and freshness signals, and frame outputs as educational market context rather than financial advice.]

## Skill Version(s):

0.4.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
