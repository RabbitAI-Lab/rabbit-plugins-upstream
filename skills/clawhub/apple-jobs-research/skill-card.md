## Description:

Researches Apple job postings via the Crawlora API, searches jobs.apple.com, pulls full posting detail including description, qualifications, location, and team, and returns clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and researchers use this skill to search Apple public careers listings, inspect hiring by team or location, and retrieve full public job posting details from specific requisition or pipeline role IDs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call endpoints beyond the Apple Jobs paths, which may send unrelated user content through the user's API key.

Mitigation: Restrict agent use to /apple-jobs/search and /apple-jobs/job, and review calls before execution.

Risk: Search terms, locations, and job IDs are sent to Crawlora with the user's API key.

Mitigation: Use the skill only when that data sharing is acceptable, and do not place secrets or unrelated user content in queries or request bodies.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance, JSON]

**Output Format:** [JSON responses with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and should be limited to Apple Jobs search and job detail endpoints.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
