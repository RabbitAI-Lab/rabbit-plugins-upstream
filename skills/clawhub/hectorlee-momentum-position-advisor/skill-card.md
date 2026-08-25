## Description:

Analyzes stock position momentum from price and volume data to produce hold, watch, reduce, sell, or add-position guidance with scoring and pattern signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiyanjun](https://clawhub.ai/user/xiyanjun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and finance-focused agents use this skill to evaluate existing stock positions from price-volume momentum, portfolio cost, and sector context. The output supports analysis-oriented position review rather than automated trade execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The output could be mistaken for investment or trading instructions.

Mitigation: Treat results as analysis only and review them with human judgment before making financial decisions.

Risk: The skill can read local position data and save local previous-decision history.

Mitigation: Review local portfolio and history files before use, and avoid storing sensitive account data in skill-managed files.

Risk: Market-data fetches or reused providers may be unavailable, delayed, or inaccurate.

Mitigation: Use the skill only where outbound market-data access is acceptable and verify important signals against trusted data sources.

## Reference(s):

- [Pattern Rules](references/pattern_rules.md)
- [ClawHub Skill Page](https://clawhub.ai/xiyanjun/skills/hectorlee-momentum-position-advisor)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Terminal text or Markdown-style analysis with stock symbols, scores, signal labels, and decision guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read local portfolio data and fetch market data; no hidden trading execution is evidenced.]

## Skill Version(s):

1.3.8 (source: frontmatter, manifest, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
