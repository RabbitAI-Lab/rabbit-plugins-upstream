## Description:

Analyzes public BBB complaint narratives, response threads, statuses, and reporting-window totals through Crawlora to compare business complaint patterns with source and coverage limits preserved.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and business analysts use this skill to compare public BBB complaint themes and business response patterns across identified businesses while preserving source attribution and reporting-window limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials and BBB search terms or profile URLs are sent to Crawlora.

Mitigation: Use a dedicated API key and share only the business scope and URLs needed for the research.

Risk: Overbroad searches or excessive pages may consume credits or collect unnecessary records.

Mitigation: Bound business scope, page count, and credit budget before retrieving results.

Risk: Incomplete complaint lists or unmatched reporting windows can lead to misleading comparisons.

Mitigation: Disclose missing detail, distinguish sample counts from aggregate totals, and preserve source dates and denominators.

## Reference(s):

- [BBB endpoint reference](reference/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/business-complaint-pattern-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown report with evidence tables and theme/status counts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes business identity, source links and dates, itemized sample sizes, aggregate reporting windows, missing coverage, and unresolved questions.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
