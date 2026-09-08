## Description:

Discovers fitness studios, wellness brands, and gym businesses on TikTok using apidojo's TikTok Scraper on Apify, returning video data, channel information, hashtags, and engagement metrics for prospecting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, partnership, and business development teams use this skill to discover and rank fitness studios, wellness brands, gyms, and personal trainers active on TikTok for targeted outreach or partnership research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok prospecting results may include personal or consumer accounts mixed with business targets.

Mitigation: Keep searches business-focused, apply filters such as follower thresholds and business-relevant keywords, and avoid unnecessary collection of non-business data.

Risk: Using Apify to query TikTok and store prospecting results can create platform, privacy, or marketing-compliance obligations.

Mitigation: Confirm Apify and TikTok terms before use, limit maxItems to the business need, protect APIFY_TOKEN, and review outreach workflows against applicable privacy and marketing rules.

Risk: High TikTok views can overstate lead quality for viral one-off content.

Mitigation: Balance views with followers, engagement rate, verification status, and deduplication by channel username before prioritizing outreach.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-fitness-brands-on-tiktok)
- [Apify TikTok Scraper run endpoint](https://api.apify.com/v2/acts/apidojo~tiktok-scraper/runs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with shell and REST API examples; downstream Apify results may be JSON or CSV.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns TikTok video and channel fields, engagement metrics, hashtags, and lead-quality tier labels when the user applies the documented scoring approach.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
