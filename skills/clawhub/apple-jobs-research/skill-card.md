## Description:

Researches Apple job postings via the Crawlora API, searching jobs.apple.com and retrieving full posting details as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search Apple's public careers listings by role, team, location, or job id and fetch full posting details for recruiting or market research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-directed job search queries to Crawlora as a third-party service.

Mitigation: Use it only when sharing the query with Crawlora is acceptable, and avoid sensitive text in query or body content.

Risk: The helper requires a Crawlora API key.

Mitigation: Store the key only in CRAWLORA_API_KEY, keep it private, and do not hardcode, commit, or pass it as a query parameter.

Risk: Search results are limited to public Apple postings and search results are metadata-only.

Mitigation: Fetch individual job details with /apple-jobs/job when full descriptions or qualifications are needed.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora API key signup](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/apple-jobs-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and only calls documented Apple Jobs endpoints.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
