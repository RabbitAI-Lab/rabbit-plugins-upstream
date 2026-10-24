## Description:

Builds evidence-backed TikTok trend briefs from current feeds, Creative Center rankings, hashtag data, and Explore categories through Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, marketers, and developers use this skill to compare TikTok topics, hashtags, and discovery feeds and produce dated, source-linked trend briefs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok research queries and the Crawlora API key are sent to Crawlora.

Mitigation: Use a dedicated key kept in the environment, avoid sensitive business details in queries, and rotate the key if exposed.

Risk: Partial or personalized samples can be mistaken for platform-wide trends.

Mitigation: Report the source surface, filters, retrieval time, sample size, and coverage limits; compare only matching scopes.

## Reference(s):

- [TikTok Trend Research on ClawHub](https://clawhub.ai/crawlora-org/skills/tiktok-trend-research)
- [Crawlora TikTok endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Concise Markdown brief or table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes retrieval time, source links or IDs, filters, sample size, and coverage caveats.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
