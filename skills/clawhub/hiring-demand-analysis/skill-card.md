## Description:

Compare advertised hiring demand across roles, skills, locations, and seniority using Crawlora's jobs dataset, with coverage and compensation-unit controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, workforce planners, and labor-market analysts use the skill to compare observed job postings across roles, employers, locations, skills, seniority, remote work, and disclosed pay. Reports define the sampled population and distinguish observed advertisements from actual hires or total labor-market demand.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Job-search queries and the Crawlora API key are sent to Crawlora.

Mitigation: Confirm that this disclosure is acceptable before use, keep the key in the environment, and omit sensitive personal or confidential business information from queries.

Risk: Unbounded samples, duplicated postings, or mixing live discovery with stored dataset counts can misstate hiring demand.

Mitigation: Bound the analysis, deduplicate eligible postings, specify denominators and coverage, and report Google Jobs discovery samples separately.

Risk: Advertised salary ranges can be misleading when disclosure is sparse or currencies and pay periods differ.

Mitigation: Report pay-disclosure coverage and compare compensation only after checking currency and pay period.

## Reference(s):

- [Hiring Demand Analysis on ClawHub](https://clawhub.ai/crawlora-org/skills/hiring-demand-analysis)
- [Crawlora jobs endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown with counts, proportions, cited example postings, and limitations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defines the cohort, observation date, coverage, exclusions, and denominator; separates current search samples from stored dataset counts.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
