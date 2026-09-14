## Description:

Research public TikTok profiles, videos, comments, hashtags, search results, trending feeds, and Creative Center signals through Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, marketers, and agents use this skill to gather bounded public TikTok evidence for profile, video, comment, hashtag, search, trending, Creative Center, and Top Ads questions through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends TikTok handles, keywords, IDs, filters, and related research inputs to Crawlora using the user's Crawlora API key.

Mitigation: Use the skill only for public TikTok research, keep the API key in an environment variable or secret store, and do not paste secrets into prompts, logs, URLs, or saved files.

Risk: Returned TikTok feed, search, Creative Center, and Top Ads samples can be partial, time-dependent, or gated.

Mitigation: Report retrieval time, filters, sample size, source URLs or stable IDs, and label hypotheses or partial results clearly.

## Reference(s):

- [tiktok-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/tiktok-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or text with source URLs, stable IDs, retrieval time, filters, sample size, and optional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded Crawlora API results and clearly labeled partial results or hypotheses.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
