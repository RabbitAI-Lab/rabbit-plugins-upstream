## Description:

Analyzes public BBB complaint narratives, response threads, statuses, and reporting-window totals to compare business complaint patterns using Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and business analysts use this skill to compare public BBB complaint themes and response processes across identified businesses while preserving source attribution, reporting windows, and gaps in complaint coverage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora receives the API key and BBB-related search parameters or profile URLs.

Mitigation: Use a scoped key, rotate it if exposed, and review Crawlora's data handling terms before researching sensitive matters.

Risk: Incomplete complaint lists or mismatched reporting windows can produce misleading comparisons.

Mitigation: Show the itemized sample and aggregate totals separately, disclose missing coverage, and compare only like-for-like periods and statuses.

Risk: Complaint allegations or response statuses may be mistaken for verified wrongdoing or outcomes.

Mitigation: Attribute each account and status to its source, retain redactions, and avoid inferring fraud, liability, or complaint rates from these records.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/business-complaint-pattern-analysis)
- [Crawlora BBB endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown with evidence tables and attributed findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes business identity, coverage and reporting windows, complaint themes and statuses, source references, and unresolved questions.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
