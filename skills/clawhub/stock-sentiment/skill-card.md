## Description:

Sentiment and smart-money positioning for US stocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and analysts use this skill to review US stock sentiment, market mood, insider and institutional activity, analyst actions, and related news as educational context, not personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API key and stock-related queries are sent to SentiSense.

Mitigation: Supply the key through the environment, keep it out of output, and allow requests only to app.sentisense.ai.

Risk: Sentiment, preview-limited data, and delayed prices could be mistaken for complete or live trading signals.

Mitigation: Label data age and preview limitations, verify figures against current responses, and frame results as context rather than investment advice.

## Reference(s):

- [Stock Sentiment on ClawHub](https://clawhub.ai/thesentitrader/skills/stock-sentiment)
- [SentiSense API skill documentation](https://sentisense.ai/skill.md)
- [SentiSense](https://sentisense.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown with dated figures and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Informational, read-only market context; not investment advice.]

## Skill Version(s):

0.4.5 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
