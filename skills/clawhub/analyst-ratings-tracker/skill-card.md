## Description:

Tracks Wall Street analyst ratings and price targets, including coverage, upgrades and downgrades, analyst call history, Street-versus-crowd comparisons, and post-earnings rating moves through the read-only SentiSense API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to gather read-only analyst coverage, rating-change, price-target, analyst-history, earnings-reaction, and SentiSense sentiment context for US stock research. It is for informational market context and not for trading, portfolio management, or personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticker research queries and the SENTISENSE_API_KEY are sent to SentiSense.

Mitigation: Confirm the user is comfortable using the external SentiSense service, store the API key only in approved secret or environment-variable handling, and avoid exposing it in logs or shared transcripts.

Risk: Financial research output could be mistaken for personalized investment advice.

Mitigation: Present results as informational market context only, preserve stated denominators and timestamps, and avoid buy, sell, price-prediction, or portfolio-management recommendations.

Risk: The npx workflow executes the external sentisense CLI package.

Mitigation: Use the pinned sentisense@0.51.0 command from the artifact or choose direct REST calls after separately reviewing the CLI package.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API](https://app.sentisense.ai)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/analyst-ratings-tracker)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with API endpoints, CLI commands, and optional JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only financial research context; requires SENTISENSE_API_KEY; outputs are informational and not investment advice.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
