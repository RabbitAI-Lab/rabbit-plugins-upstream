## Description:

Research TikTok Creative Center Top Ads by brand, market, industry, and objective through Crawlora for competitor-ad comparisons, creative briefs, messaging and format analysis, and inspection of public ad-performance charts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and analysts use this skill to query public TikTok Creative Center Top Ads through Crawlora and produce sourced comparisons of competitor ads, creative patterns, public performance signals, and repeatable research filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries send brands, keywords, countries, objectives, and related research inputs to Crawlora.

Mitigation: Use the skill only when sending those public-ad research inputs to Crawlora is acceptable for the task.

Risk: The skill requires a Crawlora API key.

Mitigation: Store CRAWLORA_API_KEY in an environment variable or secret store and avoid pasting it into chats or logs.

Risk: Public Top Ads samples and performance charts can be misread as complete campaign coverage or proof of causality.

Mitigation: Report the exact filters, preserve metric labels and units, verify advertiser identity where available, and frame proposed creative tests as hypotheses.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/tiktok-ad-research)
- [Crawlora Publisher Profile](https://clawhub.ai/user/crawlora-org)
- [Endpoint Reference](artifact/reference/endpoints.md)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown research comparison with inline shell commands and returned JSON fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes material IDs, advertiser or title where available, source links, country, objective, lookback window, duration, observed messaging or format, returned performance fields, retrieval time, and caveats for missing or uncertain observations.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
