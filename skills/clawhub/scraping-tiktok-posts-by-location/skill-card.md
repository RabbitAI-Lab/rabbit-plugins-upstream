## Description:

Extracts TikTok posts tagged at a specific location through apidojo's TikTok Location Scraper on Apify and returns post metrics, creator details, hashtags, timestamps, and media links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External teams, local marketers, event researchers, and geo-targeting analysts use this skill to collect TikTok posts associated with a TikTok place or location URL for downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Apify and sends TikTok location URLs and scrape limits to an external service.

Mitigation: Use an approved Apify account token, share only intended location URLs, and set maxItems deliberately to control data scope and cost.

Risk: The example local helper command references scripts/run_actor.js, which may not be trustworthy in every environment.

Mitigation: Review any local helper script before execution, or use the documented REST API or approved Apify MCP path instead.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-tiktok-posts-by-location)
- [Apify TikTok Location Scraper actor](https://apify.com/apidojo/tiktok-location-scraper)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Guidance]

**Output Format:** [Markdown with bash examples and CSV or JSON export options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns TikTok post metadata including captions, engagement counts, creator details, hashtags, timestamps, video URLs, audio details, and post URLs.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
