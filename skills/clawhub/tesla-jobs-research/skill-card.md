## Description:

Researches Tesla job postings via the Crawlora API, searches Tesla's careers site by title, department, or location, and retrieves a single posting's full description by id as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and recruiting researchers use this skill to search Tesla public job postings by role, department, or location and retrieve detailed job descriptions by posting id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call arbitrary Crawlora API paths and methods, which is broader than the Tesla jobs use case.

Mitigation: Review or constrain scripts/crawlora.sh to /tesla-jobs/list and /tesla-jobs/job before use.

Risk: The skill depends on CRAWLORA_API_KEY for API access.

Mitigation: Keep CRAWLORA_API_KEY in the environment only and out of files, logs, query strings, and commits.

## Reference(s):

- [Tesla Jobs endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/tesla-jobs-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY. List results are paginated and metadata-only until a job detail lookup is requested.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
