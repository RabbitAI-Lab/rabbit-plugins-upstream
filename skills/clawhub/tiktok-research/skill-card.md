## Description:

Researches TikTok profiles, videos, hashtags, search, trending content, and Creative Center ads intelligence via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and researchers use this skill to query public TikTok profile, video, hashtag, trend, comment, and Creative Center ad intelligence through Crawlora and receive normalized JSON for analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora API key can be sent to a configurable API base.

Mitigation: Do not set CRAWLORA_API_BASE unless the destination is fully trusted; keep the key in CRAWLORA_API_KEY and never hardcode, log, or commit it.

Risk: The helper can call arbitrary Crawlora paths beyond the advertised TikTok scope.

Mitigation: Review commands before execution and prefer a version that restricts the helper to documented /tiktok endpoints before using a real API key.

Risk: TikTok handles, keywords, hashtags, video IDs, and ad-research queries are sent to Crawlora.

Mitigation: Use the skill only when sending those research inputs to Crawlora is acceptable for the user's workflow.

## Reference(s):

- [tiktok-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/tiktok-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora requests and returns public TikTok data only.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
