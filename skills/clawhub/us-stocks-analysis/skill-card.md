## Description:

Provides read-only US equity research through quick data briefs and an adversarial investment committee that weighs sourced evidence and disagreements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and researchers use this skill to examine US stocks, compare bull and bear cases, and review price, sentiment, institutional activity, and fundamentals. Its findings support research rather than personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires a SentiSense API key and read-only requests to app.sentisense.ai.

Mitigation: Provide a key only if you are comfortable with that access; protect the credential and allow requests only to the disclosed service.

Risk: Free-tier previews may show only part of a dataset, and market data may be stale.

Mitigation: Label partial results, check as-of timestamps, and avoid presenting missing preview entries as absent from the full dataset.

Risk: Stock analysis could be mistaken for personalized investment advice or trading instructions.

Mitigation: Treat results as research support, verify important claims, and make investment decisions independently.

## Reference(s):

- [SentiSense API reference](https://sentisense.ai/skill.md)
- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/us-stocks-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown research briefs or evidence-backed committee verdicts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source dates, cited evidence, and explicit uncertainty; does not execute trades.]

## Skill Version(s):

2.10.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
