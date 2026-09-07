## Description:

Queries Crawlora's pre-built hosted datasets across markets, apps, social profiles, jobs, housing, maps businesses, books, games, companies, and other public-data corpora through dataset search, facets, item, and nearby endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to query Crawlora's hosted dataset indexes for bulk research, aggregate faceting, filtered search, nearby lookups, and single-record retrieval without live-crawling each source platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper makes external requests to Crawlora using the user's API key and request contents.

Mitigation: Install only when that data sharing is acceptable, use a limited and revocable Crawlora API key, and rotate the key if it may have been exposed.

Risk: The helper allows CRAWLORA_API_BASE to override the default API endpoint, which could send the API key and request contents to an untrusted service.

Mitigation: Leave CRAWLORA_API_BASE unset unless it points to a trusted HTTPS Crawlora endpoint controlled by the expected service.

## Reference(s):

- [Crawlora dataset endpoint reference](reference/endpoints.md)
- [Crawlora website](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/crawlora-datasets)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; dataset responses are paginated and refreshed periodically rather than real-time.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
