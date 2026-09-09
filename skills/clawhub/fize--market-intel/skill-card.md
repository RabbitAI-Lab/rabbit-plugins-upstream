## Description:

Generates objective market intelligence briefings covering macro policy news, overnight cross-market data, sector fund flows, and large-trade activity without trading advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fize](https://clawhub.ai/user/fize)

### License/Terms of Use:

MIT-0

## Use Case:

External users and market-research agents use this skill to collect factual market context before investment-research workflows. It formats verified macro, cross-market, fund-flow, and large-trade information into a standardized briefing while avoiding predictions and trading recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial data and market news can become stale quickly.

Mitigation: Review timestamps and source citations before relying on the briefing, and treat the output as factual context rather than trading advice.

Risk: A briefing could become misleading if required market facts cannot be retrieved or verified.

Mitigation: Follow the skill's fail-fast behavior: stop report generation and state the missing data instead of filling gaps with unsupported claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fize/skills/market-intel)
- [ClawHub publisher profile](https://clawhub.ai/user/fize)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown briefing with tables, bullets, source labels, and citations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires current external market or news data and blocks output when critical facts cannot be verified.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
