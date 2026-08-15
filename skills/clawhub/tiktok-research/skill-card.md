## Description:

Researches public TikTok profiles, videos, hashtags, search, trending content, and Creative Center ads intelligence through the Crawlora API, returning normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and marketing analysts use this skill to retrieve public TikTok creator, video, hashtag, trend, comment, and Creative Center ads data for creator vetting, trend research, and competitor ad analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok research queries and returned data are processed by Crawlora as a third-party API service.

Mitigation: Use this skill only when third-party processing is acceptable, and avoid sending sensitive payloads.

Risk: The helper can send the Crawlora API key and arbitrary requests to a configurable API base URL.

Mitigation: Keep the API key limited, leave CRAWLORA_API_BASE unset unless the destination is fully trusted, and review commands before execution.

Risk: API usage may consume Crawlora credits.

Mitigation: Monitor API usage or credits during research workflows.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/tiktok-research)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public TikTok and Creative Center data through Crawlora; list and search endpoints may require cursor pagination.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
