## Description:

Researches Upwork job postings and freelancer profiles via the Crawlora API, returning normalized JSON for job search, job-detail lookup, and freelancer-profile research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and hiring teams use this skill to search public Upwork job postings, inspect a specific posting, estimate market rates from search results, or review public freelancer profile and feedback data before outreach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call a broader API surface than the Upwork-only use case described by the skill.

Mitigation: Keep agent calls limited to /upwork/search, /upwork/job/{id}, and /upwork/freelancer/{id}; review commands before execution.

Risk: Use of Crawlora requires an API key and can consume account credits.

Mitigation: Store the key only in CRAWLORA_API_KEY, use a scoped or disposable key when possible, and monitor credit usage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/upwork-research)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a CRAWLORA_API_KEY environment variable and limits intended use to public Upwork search, job, and freelancer endpoints.]

## Skill Version(s):

1.0.1 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
