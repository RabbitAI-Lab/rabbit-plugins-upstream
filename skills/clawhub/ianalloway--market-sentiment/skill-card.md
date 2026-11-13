## Description:

Analyze market sentiment for stocks and crypto using Reddit, news headlines, and fear/greed indicators. Get a quick read on crowd psychology before trading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ianalloway](https://clawhub.ai/user/ianalloway)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and traders can use the skill to review crowd sentiment for stocks and crypto through Reddit mentions, headline tone, fear and greed readings, and volatility indicators before making trading decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reddit lookups disclose the selected ticker to Reddit.

Mitigation: Avoid querying tickers whose lookup would disclose sensitive information.

Risk: Illustrative headlines and market values, and the resulting heuristic scores, can be mistaken for current or reliable signals.

Mitigation: Replace examples with current data and treat scores as rough context rather than a trading decision.

Risk: External service availability was not tested.

Mitigation: Check that each service responds and its data is current before interpreting results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ianalloway/skills/market-sentiment)
- [Publisher profile](https://clawhub.ai/user/ianalloway)
- [Skill homepage](https://github.com/ianalloway/openclaw-skills)
- [Alternative.me Fear & Greed API](https://api.alternative.me/fng/?limit=7)
- [Reddit search API](https://www.reddit.com/r/{sub}/search.json?q={ticker}&sort=new&limit=25&t=day)

## Skill Output:

**Output Type(s):** [Analysis, Text, Shell commands]

**Output Format:** [Text sentiment summaries and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directional scores are heuristic and depend on current external data.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
