## Description:

Finds TikTok UGC creators for brand campaigns using apidojo's TikTok scrapers on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External brand teams, e-commerce teams, DTC companies, and influencer marketing managers use this skill to discover, enrich, and score TikTok micro-creators for UGC campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok search terms and profile URLs are sent to Apify.

Mitigation: Use the skill only when sending that campaign discovery data to Apify is acceptable.

Risk: APIFY_TOKEN exposure could allow unauthorized Apify usage.

Mitigation: Store APIFY_TOKEN as a secret, avoid sharing live tokens in chats or screenshots, and prefer MCP or header-based authentication over URL query tokens.

Risk: Large scraping runs can increase cost and data volume.

Mitigation: Set reasonable maxItems limits before running the TikTok scraper actors.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-tiktok-ugc-creators-for-brands)
- [apidojo/tiktok-scraper Apify actor](https://apify.com/apidojo/tiktok-scraper)
- [apidojo/tiktok-profile-scraper Apify actor](https://apify.com/apidojo/tiktok-profile-scraper)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown roster tables with inline shell commands and optional JSON or CSV result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes creator handles, follower counts, average views, engagement rates, niches, example content, UGC scores, and tier classifications.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
