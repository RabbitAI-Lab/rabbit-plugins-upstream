## Description:

Researches TikTok profiles, videos, hashtags, search, trending content, and Creative Center ads intelligence via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and researchers use this skill to query public TikTok profile, video, hashtag, trend, comment, and Creative Center advertising intelligence through Crawlora instead of scraping TikTok directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key and sends TikTok handles, keywords, video IDs, and ad research queries to Crawlora.

Mitigation: Install only if this data sharing is acceptable, keep the key in CRAWLORA_API_KEY, and do not hardcode, place in URLs, or commit the key.

Risk: The helper script can call broader Crawlora API paths beyond the documented TikTok research use case.

Mitigation: Review requested paths before execution and restrict use to the documented TikTok endpoints unless broader Crawlora access is intended.

Risk: Creative Center results can be partial because anonymous hashtag and video endpoints are limited and country coverage can be uneven.

Mitigation: Report query parameters and known endpoint limits with results, and avoid treating empty or short Creative Center responses as exhaustive market coverage.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/tiktok-research)
- [Publisher profile](https://clawhub.ai/user/tonywangcn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requested TikTok handles, keywords, video IDs, and ad queries to Crawlora.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
