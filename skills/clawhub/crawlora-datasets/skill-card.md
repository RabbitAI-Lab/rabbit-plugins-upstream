## Description:

Queries Crawlora's pre-built hosted datasets via search, facets, item, and nearby endpoints, returning JSON for bulk analysis, aggregate questions, filtered search, and record lookup without live-crawling each source platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to query Crawlora's hosted public datasets for market research, entity discovery, faceted aggregate analysis, and individual record lookup. It is best suited for pre-indexed dataset questions rather than real-time single-page lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call broader Crawlora API paths with arbitrary methods and request bodies, not only documented dataset GET endpoints.

Mitigation: Review intended calls before use and prefer documented /datasets GET endpoints for dataset-read workflows.

Risk: Queries, filters, and JSON bodies are sent to Crawlora's API.

Mitigation: Use only data you are comfortable sending to Crawlora and avoid secrets or confidential investigative terms in request parameters or bodies.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora website](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/crawlora-datasets)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with shell command examples that return JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns paginated Crawlora API responses.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
