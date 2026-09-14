## Description:

Build evidence-backed TikTok trend briefs from current feeds, Creative Center rankings, hashtag data, and Explore categories through Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, research, and social intelligence users can use this skill to compare TikTok trend surfaces for a topic, hashtag, category, country, or lookback period. The skill helps produce dated, sample-aware briefs that separate observed ranking data from interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper sends TikTok research queries and a Crawlora API key to Crawlora.

Mitigation: Use the API key from an environment variable, keep it private, and review query or body values before running the helper.

Risk: Trend outputs can be mistaken for complete TikTok coverage even when the available sample is partial or surface-specific.

Mitigation: Report the trend surface, filters, sample size, retrieval time, and coverage caveats with each brief.

Risk: Empty or limited API responses can lead to overconfident conclusions.

Mitigation: Inspect HTTP status and JSON envelope values, preserve partial results, and label missing observations instead of fabricating conclusions.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/tiktok-trend-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Concise Markdown brief or table with source IDs, filters, retrieval time, and coverage caveats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Crawlora helper commands and guidance for interpreting returned JSON.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
