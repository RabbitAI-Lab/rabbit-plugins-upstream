## Description:

Runs SERP and keyword research via the Crawlora API for Google, Bing, Brave, DuckDuckGo, Yahoo, and Google Trends, returning normalized JSON for rankings, SERP snapshots, autocomplete suggestions, and trend data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO practitioners, and research agents use this skill to collect public search result snapshots, keyword suggestions, and Google Trends signals through Crawlora instead of scraping search result pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search and trend requests are sent to Crawlora along with the configured API key.

Mitigation: Use the skill only when sharing those requests with Crawlora is acceptable, and keep the key in CRAWLORA_API_KEY rather than hardcoding or committing it.

Risk: The CRAWLORA_API_BASE override could send the Crawlora API key to an unintended endpoint if the environment is influenced.

Mitigation: Review or remove CRAWLORA_API_BASE before use and send authenticated requests only to the trusted Crawlora API base.

Risk: The endpoint reference covers broader Crawlora API access than keyword research, including finance, jobs, maps, and local-business data.

Mitigation: Limit calls to task-relevant public SERP, keyword, and trends endpoints unless the broader data access is explicitly needed.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell command examples and normalized JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; calls are sent to the Crawlora API and may use GET query parameters or POST JSON bodies.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
