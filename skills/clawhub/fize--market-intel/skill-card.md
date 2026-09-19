## Description:

Market Intel helps agents gather and verify macro, cross-market, fund-flow, and block-trade facts, then produce a factual market intelligence briefing without trading advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fize](https://clawhub.ai/user/fize)

### License/Terms of Use:

MIT-0

## Use Case:

External users and market research agents use this skill to collect current public market and news facts, verify sources and timestamps, classify each item, and produce a standardized market intelligence briefing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market and news data can be stale, unavailable, or inconsistent across public sources.

Mitigation: Verify each cited source, publication time, market timestamp, scope, unit, and reconciliation result; stop briefing generation when required facts cannot be verified.

Risk: A factual market briefing may be misread as investment advice.

Mitigation: Keep outputs limited to objective facts and evidence, and avoid forecasts, subjective trading views, recommendations, or trade execution instructions.

## Reference(s):

- [market-intel skill page](https://clawhub.ai/fize/skills/market-intel)
- [fize publisher profile](https://clawhub.ai/user/fize)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown market intelligence briefing with source labels, timestamps, factual tables, and concise bullet summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill requires verified market and news data, blocks report generation when key facts cannot be verified, and avoids forecasts, trading opinions, and trade execution guidance.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
