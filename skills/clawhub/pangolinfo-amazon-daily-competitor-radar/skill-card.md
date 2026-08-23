## Description:

Monitors an Amazon ASIN against nearby competitors, category movers, price and Buy Box changes, reviews, and new entrants to produce a daily competitor radar with action recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pangolinfo](https://clawhub.ai/user/pangolinfo)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and growth teams use this skill to monitor daily competitive movement around a target ASIN, identify ranking, pricing, Buy Box, review, and category-entry signals, and decide immediate defensive or counter actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Pangolinfo-backed Amazon market data tools and repeatedly look up product and competitor information.

Mitigation: Install and run it only when that data access is appropriate for the user's Amazon monitoring workflow.

Risk: Optional daily scheduling can create recurring runs, credit usage, and repeated product lookups.

Mitigation: Enable the schedule only after explicit user intent and review the resulting cron or CronCreate entry.

Risk: Per-ASIN baseline snapshots may be stored locally for day-over-day comparison.

Mitigation: Keep snapshots in the documented local baseline location and remove them when monitoring is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pangolinfo/skills/pangolinfo-amazon-daily-competitor-radar)
- [Pangolinfo](https://www.pangolinfo.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with concise action recommendations and optional scheduling snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May maintain per-ASIN baseline snapshots locally when the agent has filesystem access.]

## Skill Version(s):

4.0.0 (source: server release metadata; artifact frontmatter says 3.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
