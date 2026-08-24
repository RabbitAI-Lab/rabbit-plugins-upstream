## Description:

Queries Crawlora's pre-built hosted datasets for bulk, aggregate, and record-level research through search, facets, item, and nearby endpoints, returning JSON without live-crawling each source platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to query Crawlora's hosted public datasets for population-level analysis, filtered search, aggregate facets, nearby lookups, and individual dataset records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can call Crawlora API paths beyond the hosted-dataset endpoints described by the skill.

Mitigation: Review the helper before installation and restrict, edit, or wrap it locally if the deployment should only allow dataset endpoints.

Risk: Crawlora API keys may be exposed if hardcoded, committed, or passed through URLs.

Mitigation: Store the key only in CRAWLORA_API_KEY or a managed secret store, avoid query-string secrets, and rotate the key if exposure is suspected.

Risk: Hosted datasets are refreshed periodically rather than in real time.

Mitigation: Use the skill for public, non-sensitive dataset research and verify freshness before relying on results for time-sensitive decisions.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY; results are paginated and datasets refresh periodically.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
