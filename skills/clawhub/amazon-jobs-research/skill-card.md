## Description:

Researches Amazon.jobs postings via the Crawlora API — search Amazon's public careers site by keyword or job category, then fetch a single posting's full description and qualifications by job id as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and job-search assistants use this skill to search public Amazon.jobs postings, browse Amazon job categories, sort by recent postings, and fetch full details for a known Amazon job id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can call authenticated Crawlora endpoints beyond the Amazon Jobs endpoints, which may use the API key and credits outside the skill's stated purpose.

Mitigation: Review proposed calls before execution and prefer a version that restricts the helper to /amazon-jobs/search and /amazon-jobs/job.

Risk: The skill requires a Crawlora API key for requests.

Mitigation: Keep the key in CRAWLORA_API_KEY and do not hardcode, pass as a query parameter, or commit it.

## Reference(s):

- [Amazon Jobs endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora API calls; Amazon Jobs search results are paginated.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
