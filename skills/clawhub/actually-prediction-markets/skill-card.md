## Description:

Use when a claim about the future comes up and you want a number instead of a guess - elections, rate decisions, sports, court dates, releases. Looks up what a Polymarket prediction market is currently pricing for that exact claim.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sofiia7](https://clawhub.ai/user/sofiia7)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn future-event claims from headlines, conversations, or summaries into market-implied probabilities. It helps agents report the matched market question, probability, confidence, and alternatives instead of presenting an unsupported guess.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional trading mode can place real orders if POLYMARKET_PRIVATE_KEY is configured.

Mitigation: Leave POLYMARKET_PRIVATE_KEY unset for read-only use, and enable it only after reviewing the external package/source and confirming the operator intends to allow real orders.

Risk: Semantic matching can select a related-but-different market for a thin or ambiguous claim.

Mitigation: Show the matched market question, confidence, and alternatives so users can judge whether the quoted probability answers the original claim.

Risk: Prediction-market prices can be noisy or wrong and should not be presented as authoritative forecasts.

Mitigation: Describe probabilities as market-implied signals, include relevant context, and avoid treating the price as a guarantee.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sofiia7/skills/actually-prediction-markets)
- [Source and threat model](https://github.com/Sofiia7/actually)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and market probability summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only probability lookup needs no account; optional trading requires operator configuration and explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
