## Description:

Screens US stocks and ETFs against sentiment, analyst, price, technical, momentum, and end-of-day options signals using custom criteria or curated screens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use the skill to find and compare US stocks or ETFs matching natural-language screening criteria or ready-made screens, including screens limited to a watchlist. Results support market research rather than investment recommendations or trading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key and requested watchlist or screening tickers are sent to SentiSense.

Mitigation: Share only intended tickers and keep the API key private; use it solely for read-only market research.

Risk: Screening results can be mistaken for live prices or personalized investment advice.

Mitigation: Label results as snapshot-based, check the source dates, and do not use the skill to place trades or make personalized recommendations.

## Reference(s):

- [ClawHub stock-screener release](https://clawhub.ai/thesentitrader/skills/stock-screener)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown describing screening criteria, matching stocks or ETFs, and result counts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results; screening prices are snapshots, not live quotes.]

## Skill Version(s):

1.4.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
