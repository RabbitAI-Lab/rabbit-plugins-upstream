## Description:

Researches Apple job postings through the Crawlora API, searching jobs.apple.com and returning normalized JSON with posting details such as description, qualifications, location, and team.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Apple's public careers listings, inspect hiring by role, team, or location, and retrieve full posting details for a specific Apple job id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Apple job search requests and the Crawlora API key to Crawlora as an intermediary.

Mitigation: Install only if that intermediary is acceptable, store the key in CRAWLORA_API_KEY, and do not hardcode or commit it.

Risk: Search results include metadata only and may be incomplete if users do not paginate or fetch job details.

Mitigation: Page through search results and call the job detail endpoint for postings that need full descriptions and qualifications.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; search results are metadata-only until the job detail endpoint is called.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
