## Description:

Research public TikTok profiles, videos, comments, hashtags, search results, trending feeds, and Creative Center signals through Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect and interpret public TikTok profile, video, comment, hashtag, search, trending, Creative Center, and Top Ads data through Crawlora's API. It is suited to bounded TikTok discovery, verification, and comparison tasks where results must be tied to returned public records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends TikTok handles, IDs, keywords, filters, and a Crawlora API key to Crawlora.

Mitigation: Keep the API key in the environment, avoid confidential investigation terms or unnecessary personal data, and use bounded requests.

Risk: Public TikTok samples, search results, trending feeds, and Creative Center data can be incomplete, time-dependent, or gated.

Mitigation: Report retrieval time, filters, sample size, and access limits; avoid treating samples as a complete census or as proof of cause.

Risk: Application-level errors or partial API failures can appear inside otherwise successful HTTP responses.

Mitigation: Check the JSON envelope and application code, preserve clearly labeled partial results, and stop on access failures.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/tiktok-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with optional shell command examples and structured observations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include source URLs or stable IDs, retrieval time, filters, sample size, and clear separation between observed facts and hypotheses.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
