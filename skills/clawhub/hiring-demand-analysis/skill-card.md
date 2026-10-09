## Description:

Compare advertised hiring demand across roles, skills, locations, and seniority using Crawlora's jobs dataset, with explicit controls for coverage and compensation units.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, labor-market analysts, and developers use this skill to compare observed job postings by role, skill, location, seniority, employer, remote status, and advertised pay while reporting sample coverage and limitations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Job-search queries and the API key are sent to Crawlora's API.

Mitigation: Use the skill only if this transfer is acceptable; keep CRAWLORA_API_KEY private and review POST bodies before sending.

Risk: Combining Google Jobs samples with stored dataset counts can misstate hiring demand.

Mitigation: Report the two sources separately and state each sample's coverage and denominator.

## Reference(s):

- [Jobs API endpoint reference](reference/endpoints.md)
- [Crawlora API key setup](https://crawlora.net)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/hiring-demand-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown analysis with cohort definitions, counts, cited examples, and limitations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Distinguishes stored dataset counts from separate current-search samples.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
