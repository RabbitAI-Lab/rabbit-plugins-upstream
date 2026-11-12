## Description:

Analyzes CSV market data with a four-factor sentiment model and returns a 0-100 market score, market state, and trading-context guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cqdev-ai](https://clawhub.ai/user/cqdev-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to run local CSV-based market sentiment checks, inspect score components, track short trends, and pass a market-state parameter into a stock-planning workflow. Its outputs are reference material and not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market scores, states, and suggested trading posture could be mistaken for investment advice.

Mitigation: Treat all outputs as reference material only and require independent financial judgment before making investment decisions.

Risk: Incomplete, incorrect, or unintended CSV inputs can produce misleading analysis.

Mitigation: Use only CSV files intended for analysis and verify that required market columns are present and accurate.

Risk: The optional output path writes local JSON and could overwrite a file if chosen carelessly.

Mitigation: Choose the --output path deliberately and review generated files before using them downstream.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cqdev-ai/skills/market-sentiment)
- [Artifact README](artifact/README.md)
- [Artifact skill definition](artifact/SKILL.md)
- [Sentiment analysis script](artifact/scripts/sentiment.py)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Terminal text reports with optional JSON file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads local CSV market data and can write JSON to a user-selected output path.]

## Skill Version(s):

1.1.0 (source: server release metadata, package.json, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
