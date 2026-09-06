## Description:

Pull LinkedIn person and company profiles, their posts, job listings and post comments as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, recruiting teams, sales teams, and market researchers use this skill to fetch structured LinkedIn profile, company, post, comment, and job data through Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn profile, company, post, comment, and job data may include personal or business-sensitive information.

Mitigation: Use the skill only for legitimate, policy-approved purposes; avoid bulk profiling; and store or combine only the data needed for the user's task.

Risk: Paginated endpoints and full job-detail calls consume more Scavio credits and can create unexpected cost if run in broad loops.

Mitigation: Set page limits before calling paginated endpoints, estimate credit use before execution, and call full job detail only for listings the user has selected.

Risk: The skill requires a Scavio API key.

Mitigation: Load SCAVIO_API_KEY from the environment or a secret store and keep API keys out of source code and shared transcripts.

Risk: Job search results can rotate and overlap across pages, and retired endpoints return permanent 410 responses.

Mitigation: Deduplicate job results by id, avoid describing searched pages as exhaustive, and treat 410 responses as permanently unavailable rather than retryable.

## Reference(s):

- [Scavio LinkedIn API documentation](https://scavio.dev/docs/linkedin-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=linkedin-scraper-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=linkedin-scraper-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/linkedin-scraper-api)
- [ClawHub publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown guidance with JSON request and response details, shell setup commands, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses are structured JSON and some paginated endpoints consume credits per page.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter says 2.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
