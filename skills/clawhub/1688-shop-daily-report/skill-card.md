## Description:

Generates a dated 1688 shop operating report with sales, traffic, buyer, advertising, review, anomaly, and action-priority analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1688aiinfra](https://clawhub.ai/user/1688aiinfra)

### License/Terms of Use:

MIT-0

## Use Case:

External 1688 merchants use this skill to generate daily shop performance reports, compare single-shop or multi-shop metrics, identify anomalies, and choose concrete follow-up actions. The skill is intended for business operations analysis rather than software development.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a 1688 AK and can read business, advertising, buyer, review, and bound-shop data across shops.

Mitigation: Install only for accounts where that access is acceptable, use the least-privileged AK available, and review authorization before deployment.

Risk: Bind-list outputs may expose AK-bearing data beyond what the report reader needs.

Mitigation: Strip AK fields from bind-list outputs before approval or deployment.

Risk: Free-query APIs may allow broader data reads than the documented daily-report workflow requires.

Mitigation: Constrain free-query use to documented read-only report endpoints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/1688aiinfra/skills/1688-shop-daily-report)
- [Capabilities reference](references/capabilities.md)
- [Interaction specifications](references/interaction-specs.md)
- [Wiki routing rules](references/wiki-routing-rules.md)
- [Factory profile reference](references/profiles/factory.md)
- [Integrated profile reference](references/profiles/integrated.md)
- [Trader profile reference](references/profiles/trader.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown reports with structured follow-up card options and JSON-backed command results used internally by the agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports summarize T+1 shop data and may cover one shop or multiple bound shops.]

## Skill Version(s):

0.43.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
