## Description:

Researches Tesla job postings via the Crawlora API, including searches by title, department, or location and retrieval of a single posting's full description by ID as JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, recruiters, job seekers, and developers use this skill to search public Tesla careers listings and retrieve full posting details for targeted job research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper accepts arbitrary Crawlora API paths, so an agent could use it outside the Tesla Jobs purpose of the skill.

Mitigation: Use or replace it with a wrapper that allowlists only /tesla-jobs/list and /tesla-jobs/job.

Risk: The API key could be sent to an unintended endpoint if CRAWLORA_API_BASE is overridden.

Mitigation: Do not set CRAWLORA_API_BASE for normal use, and rotate CRAWLORA_API_KEY if it may have been used with an untrusted base URL.

Risk: Search results are paginated and list responses are metadata-only, which can lead to incomplete job research.

Mitigation: Page through list results and call /tesla-jobs/job for postings that need full descriptions, responsibilities, and requirements.

## Reference(s):

- [Tesla Jobs endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/tesla-jobs-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns paginated listing metadata or full job-detail JSON.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
