## Description:

Build evidence-backed TikTok trend briefs from current feeds, Creative Center rankings, hashtag data, and Explore categories through Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to gather dated TikTok trend observations for topics, hashtags, categories, countries, or periods and turn them into concise sample-aware briefs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok research queries and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only when that data sharing is acceptable, keep the key in the environment, and avoid private or sensitive business topics unless approved by the organization.

Risk: Trend results are partial, time-sensitive samples and may not represent complete TikTok coverage.

Mitigation: Report retrieval time, surface, filters, sample size, and coverage caveats, and label conclusions as observed sample signals rather than platform-wide facts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/tiktok-trend-research)
- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown brief or table with source ids, filters, sample size, retrieval time, metrics, and coverage caveats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should distinguish observed sample signals from hypotheses, forecasts, and content recommendations.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
