## Description:

Extracts TikTok posts using a specific audio track or sound with apidojo's TikTok Music Scraper on Apify, returning post, creator, hashtag, and song metadata for downstream analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, analysts, and developers use this skill to collect TikTok videos tied to a specific sound or music URL for trend tracking, creator discovery, campaign analysis, or export into downstream datasets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apify runs may collect large result sets for trending sounds.

Mitigation: Set maxItems to cap collection size when large runs are not intended.

Risk: Inputs and outputs may include public social-media content and user metadata.

Mitigation: Avoid submitting sensitive or private URLs, and review downstream handling of collected data before sharing or storing it.

Risk: The skill requires an Apify token for API or actor execution.

Mitigation: Use a scoped Apify token and avoid exposing credentials in prompts, logs, or shared command history.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-tiktok-posts-by-music)
- [Publisher profile](https://clawhub.ai/user/apidojo-io)
- [Apify actor runs API](https://api.apify.com/v2/acts/apidojo~tiktok-music-scraper/runs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, json]

**Output Format:** [Markdown guidance with inline shell commands and JSON API input examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides Apify actor calls that can return raw TikTok post datasets with captions, engagement counts, creator details, hashtags, video metadata, and song metadata.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
