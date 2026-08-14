## Description:

Queries Crawlora's pre-built hosted datasets through search, facets, item, and nearby endpoints, returning JSON for bulk analysis, indexed-corpus search, faceting, and dataset record lookup without live-crawling each source.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to query Crawlora's pre-indexed public datasets for bulk research, aggregate and facet analysis, nearby lookup, and record retrieval instead of scraping pages one at a time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call broader Crawlora API paths than the hosted dataset endpoints described by the skill.

Mitigation: Review requested paths before execution, limit use to documented /datasets endpoints unless broader Crawlora access is intended, and tighten or clearly disclose helper scope before deployment.

Risk: The skill requires a Crawlora API key and sends requests to Crawlora's API.

Mitigation: Store the key only in CRAWLORA_API_KEY, do not commit it or pass it in query parameters, and review account and credit usage for executed requests.

Risk: Dataset results are refreshed on a schedule and may not be real-time.

Mitigation: Use a live lookup source when a task requires current single-record verification.

## Reference(s):

- [Crawlora Datasets endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora website](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/crawlora-datasets)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; responses are paginated, billed only on successful requests according to artifact notes, and sourced from datasets refreshed on a schedule.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
