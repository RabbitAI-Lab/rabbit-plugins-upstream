## Description:

Researches Apple job postings via the Crawlora API, searches jobs.apple.com, pulls full posting detail including description, qualifications, location, and team, and returns clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and researchers use this skill to search public Apple Careers postings by role, team, and location, then retrieve full details for specific requisitions or pipeline roles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can call arbitrary Crawlora API paths when invoked directly, which is broader than the Apple Jobs endpoints documented for the skill.

Mitigation: Review and restrict use to GET requests for /apple-jobs/search and /apple-jobs/job unless a broader Crawlora API client is explicitly intended.

Risk: The skill requires an authenticated Crawlora API key and sends request parameters to the Crawlora API.

Mitigation: Use a limited Crawlora key, keep it in CRAWLORA_API_KEY, and avoid passing sensitive data in query parameters or request bodies.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [guidance, shell commands, API calls, JSON]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; Apple Jobs search results are metadata-only until the job detail endpoint is called.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
