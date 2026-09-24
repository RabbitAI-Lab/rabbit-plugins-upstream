## Description:

LinkedIn API integration with a single superagnt API key for fetching company profiles, jobs, people, posts, and professional network insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve LinkedIn company, profile, job, post, article, and location data for sales, recruiting, enrichment, research, and market intelligence workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn profile URLs, usernames, company identifiers, job searches, and similar professional-data queries are sent to superagnt.

Mitigation: Submit only data that the user has a legitimate reason and permission to process, and follow applicable privacy and data-handling policies.

Risk: The SUPERAGNT_API_KEY bearer token could expose access or credits if shared or logged.

Mitigation: Keep the key private, prefer a dedicated key when available, and avoid placing it in transcripts, repositories, or shared logs.

## Reference(s):

- [LinkedIn Data documentation](https://superagnt.com/r/ch-linkedin-data-docs)
- [Dashboard and API keys](https://superagnt.com/r/ch-linkedin-data-key)
- [LinkedIn Data ClawHub listing](https://clawhub.ai/superagnt/skills/linkedin-data)
- [superagnt publisher profile](https://clawhub.ai/user/superagnt)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Guidance]

**Output Format:** [Markdown with curl commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY; sends user-directed LinkedIn data requests to superagnt.]

## Skill Version(s):

2.0.6 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
