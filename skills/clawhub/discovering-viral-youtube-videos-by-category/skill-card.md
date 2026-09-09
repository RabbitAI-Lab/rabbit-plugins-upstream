## Description:

Discovers trending and viral YouTube videos by category and country using Apidojo's YouTube Trending Scraper on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Content strategists, YouTubers, and trend researchers use this skill to find and rank trending YouTube videos by category and country for trend research and content planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires an Apify API token and may incur Apify usage costs.

Mitigation: Confirm token scope and expected actor usage before running; set maxItems to bound calls and costs.

Risk: A user-provided customMapFunction is executable transformation logic for actor output.

Mitigation: Review customMapFunction code before use and avoid passing untrusted transformations.

Risk: Trending results are a snapshot and can become stale as YouTube trends change throughout the day.

Mitigation: Record retrieval time and rerun the actor when decisions depend on current trends.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/discovering-viral-youtube-videos-by-category)
- [Apify YouTube Trending Scraper API endpoint](https://api.apify.com/v2/acts/apidojo~youtube-trending-scraper/runs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional table, JSON, or CSV results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Apify actor inputs for category, country, language, item limit, and optional output transformation; trend data is a point-in-time snapshot.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
