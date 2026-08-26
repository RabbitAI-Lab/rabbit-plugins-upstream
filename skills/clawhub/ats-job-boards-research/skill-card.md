## Description:

Fetches company job openings from ATS-hosted career pages through the Crawlora API across Greenhouse, Lever, Workday, Ashby, SmartRecruiters, Workable, Personio, Recruitee, iCIMS, Oracle Recruiting, Rippling, Pinpoint, Eightfold, Gem, UKG, and Teamtailor, returning normalized JSON for board listings, job details, and hiring-signal snapshots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external analysts, and developers use this skill to retrieve public ATS job-board listings, single posting details, and hiring-velocity snapshots for companies when the ATS platform and board slug are known or can be probed by slug.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included helper can make arbitrary authenticated Crawlora API requests beyond the documented ATS job endpoints.

Mitigation: Use the helper only for documented /jobs endpoints needed for the task, and review generated commands before execution.

Risk: The skill requires a Crawlora API key and may send prompts, company names, or query parameters to the Crawlora API.

Mitigation: Keep CRAWLORA_API_KEY in the environment only, never commit it, and avoid sending confidential company research or sensitive data.

Risk: The skill is intended for public job-board research and depends on external ATS and Crawlora API availability.

Mitigation: Use it for public postings only, respect source terms, and validate important hiring conclusions against the returned job-board data.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/ats-job-boards-research)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with inline shell commands and expected JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora API calls and returns public ATS job-board data.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
