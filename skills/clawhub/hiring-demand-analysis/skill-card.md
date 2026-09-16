## Description:

Compare advertised hiring demand across roles, skills, locations, and seniority using Crawlora's jobs dataset.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and market researchers use this skill to query Crawlora jobs data, compare advertised hiring demand across defined cohorts, and report counts, proportions, example postings, and limitations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hiring-analysis queries and the Crawlora API key are sent to Crawlora's API.

Mitigation: Install only if this data sharing is acceptable, keep CRAWLORA_API_KEY private and scoped, and avoid exposing the key in command history or shared logs.

Risk: Returned job data is a snapshot of advertised postings and may not represent hires, headcount growth, or the full labor market.

Mitigation: Define the cohort and denominator, deduplicate postings, label coverage gaps, and avoid treating posting counts as completed hires or market-wide totals.

Risk: Compensation, location, seniority, and remote-work fields can be incomplete, inferred, or not directly comparable across postings.

Mitigation: Preserve source fields, report disclosure coverage, verify currency and compensation period, and state assumptions before summarizing salary or location comparisons.

## Reference(s):

- [hiring-demand-analysis endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/hiring-demand-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and analysis guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include query definitions, coverage notes, counts, proportions, cited example postings, and limitations.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
