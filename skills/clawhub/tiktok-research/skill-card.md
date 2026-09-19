## Description:

Research public TikTok profiles, videos, comments, hashtags, search results, trending feeds, and Creative Center signals through Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, marketers, and developers use this skill to gather bounded public TikTok profile, video, comment, hashtag, trend, Creative Center, and Top Ads evidence through Crawlora. It helps produce current, source-tied research outputs while preserving filters, retrieval time, sample size, and stable IDs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends TikTok research queries to Crawlora as a third-party API provider.

Mitigation: Install and use it only when that provider relationship is appropriate for the task, and avoid private or sensitive search terms unless approved for the use case.

Risk: The helper requires CRAWLORA_API_KEY for API access.

Mitigation: Keep the key in the environment, do not place it in URLs or prompt output, and rely on the bundled helper's credential-safe curl configuration.

Risk: Large or unbounded crawls can create unnecessary API exposure and cost.

Mitigation: Use bounded requests, preserve partial results when appropriate, and stop or back off on access limits and rate-limit responses.

## Reference(s):

- [tiktok-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/tiktok-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown answers with inline shell commands and source-tied TikTok identifiers or URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include retrieval time, filters, sample size, stable IDs or source URLs, and a clear separation between observed facts and hypotheses.]

## Skill Version(s):

1.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
