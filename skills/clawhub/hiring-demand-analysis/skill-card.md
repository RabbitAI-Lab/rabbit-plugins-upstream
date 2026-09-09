## Description:

Compare advertised hiring demand across roles, skills, locations, and seniority using Crawlora's jobs dataset.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and analysts use this skill to query Crawlora jobs data and report labor-market snapshots across roles, skills, locations, employers, remote work, seniority, and advertised compensation. Outputs should define the cohort, coverage, denominator, exclusions, example postings, and limitations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper requires a Crawlora API key and makes outbound API calls.

Mitigation: Review the skill before installation, keep the key in the environment, and run the helper only in an environment where untrusted code or shell profiles cannot set CRAWLORA_API_BASE.

Risk: The API helper is broader than the stated hiring workflow and could send sensitive non-job data if misused.

Mitigation: Use the helper only for the documented jobs-analysis endpoints and avoid passing sensitive non-job data through it.

Risk: Hiring-demand outputs can be misleading if observed postings are treated as hires, headcount growth, or a complete labor-market measure.

Mitigation: Report cohort definitions, coverage, exclusions, denominators, deduplication approach, and limitations with every analysis.

## Reference(s):

- [hiring-demand-analysis endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/hiring-demand-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis with inline shell command examples and cited job-posting evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include raw JSON snippets from Crawlora API responses when needed for auditability.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
