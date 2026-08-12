## Description:

Runs SERP and keyword research via the Crawlora API for Google, Bing, Brave, DuckDuckGo, Yahoo, and Google Trends, returning normalized JSON for search rankings, keyword suggestions, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO practitioners, and market researchers use this skill to capture normalized SERP snapshots, keyword suggestions, and trend signals without scraping result pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, locations, business names, tickers, and request bodies are sent to Crawlora and may be routed to upstream public search services.

Mitigation: Avoid sensitive or confidential searches and review data-boundary requirements before using the skill in controlled environments.

Risk: The helper can send arbitrary API requests to Crawlora with the user's API key.

Mitigation: Use a dedicated low-privilege Crawlora key and prefer a scoped wrapper or endpoint allowlist for managed deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/serp-keyword-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY and sends request data to Crawlora API endpoints.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
