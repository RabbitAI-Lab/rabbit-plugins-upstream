## Description:

Runs SERP and keyword research via the Crawlora API for Google, Bing, Brave, DuckDuckGo, and Yahoo search results plus Google Trends interest-over-time and related or rising queries, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO practitioners, and analysts use this skill to capture public SERP snapshots, expand keyword ideas, and compare search trend signals through the Crawlora API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and request parameters are sent to Crawlora.

Mitigation: Use the skill for non-sensitive SERP and keyword research unless sharing those terms with Crawlora is acceptable.

Risk: The helper can call a broader Crawlora API surface than the skill name and description imply.

Mitigation: Review the endpoint reference and limit use to the expected SERP, keyword, and trend endpoints before installation.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON API responses with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends search terms and request parameters to Crawlora.]

## Skill Version(s):

1.0.5 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
