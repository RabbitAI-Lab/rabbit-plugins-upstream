## Description:

Researches public TikTok profiles, videos, hashtags, search results, trending content, and Creative Center ads intelligence through the Crawlora API and returns clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing researchers use this skill to inspect public TikTok creators, posts, comments, hashtags, trends, and Creative Center ads data without scraping TikTok directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send the Crawlora API key and query data to an arbitrary API base if CRAWLORA_API_BASE is set.

Mitigation: Keep CRAWLORA_API_BASE unset unless the destination is fully trusted, and rotate the API key if it was ever used with an untrusted API base.

Risk: TikTok research terms, profile handles, video IDs, and ad-search filters are sent to Crawlora.

Mitigation: Avoid sensitive internal terms or personal data in queries unless that use has been approved.

Risk: The skill is intended for public TikTok data and may produce incomplete Creative Center results because anonymous access is limited.

Mitigation: Use it only for public-data research, respect TikTok terms, and account for documented Creative Center result limits during analysis.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated requests; list and search endpoints may require cursor pagination.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
