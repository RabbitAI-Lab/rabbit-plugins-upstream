## Description:

Queries Crawlora's pre-built hosted datasets across markets, apps, social profiles, jobs, housing, businesses, finance, games, and other public-data corpora through search, facets, item, and nearby endpoints that return JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to query Crawlora's hosted public datasets for bulk research, aggregate analysis, filtered search, faceting, nearby lookup, and record retrieval instead of scraping pages one at a time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send the Crawlora API key to an environment-chosen API base URL.

Mitigation: Run only in an environment you control and leave CRAWLORA_API_BASE unset unless you intentionally trust the destination.

Risk: The helper supports non-dataset API paths outside the stated dataset purpose.

Mitigation: Restrict routine use to documented /datasets endpoints or clearly review and disclose any broader Crawlora API calls.

Risk: Queries may contain sensitive or proprietary search terms.

Mitigation: Avoid sending sensitive, confidential, or proprietary terms to the API.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/crawlora-datasets)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; results are paginated and dataset freshness varies by source.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
