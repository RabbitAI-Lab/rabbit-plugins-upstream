## Description:

Analyzes public BBB complaint narratives, response threads, statuses, and reporting-window totals through Crawlora to support sourced business comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and business analysts compare public BBB complaint themes and business response patterns across selected businesses, preserving source attribution, reporting windows, and coverage gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and BBB profile URLs are sent to Crawlora, and use requires a Crawlora API key.

Mitigation: Provide the key only if comfortable with the external service; bound requests to the businesses and reporting windows needed.

Risk: Incomplete complaint lists or mismatched reporting windows can distort comparisons, while allegations can be mistaken for established wrongdoing.

Mitigation: Preserve source attribution and coverage limits, compare like-for-like denominators, and treat findings as sourced research rather than proof of wrongdoing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/business-complaint-pattern-analysis)
- [Crawlora BBB endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown with sourced evidence tables and theme and status counts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates itemized coverage from aggregate totals and flags missing complaint details.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
