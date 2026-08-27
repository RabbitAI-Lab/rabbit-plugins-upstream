## Description:

Researches Amazon.jobs postings via the Crawlora API by searching Amazon's public careers site by keyword or job category and fetching a single posting's description and qualifications by job id, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and job researchers use this skill to search public Amazon.jobs postings, browse Amazon job categories, and retrieve normalized JSON details for a specific Amazon job posting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can make authenticated Crawlora API requests beyond the Amazon Jobs endpoints.

Mitigation: Review requested paths, HTTP methods, and request bodies before execution, and restrict routine use to the documented Amazon Jobs endpoints.

Risk: The Crawlora API key could be misused through broad API calls, committed secrets, query-string exposure, or untrusted CRAWLORA_API_BASE values.

Mitigation: Keep the key only in CRAWLORA_API_KEY, use a limited key if available, monitor API credit usage, and avoid letting untrusted prompts control CRAWLORA_API_BASE.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/amazon-jobs-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns paginated public Amazon.jobs posting data.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
