## Description:

Finds food content creators across Instagram, TikTok, and YouTube using apidojo's social media scrapers on Apify and returns creator handles, platform metrics, engagement signals, content themes, and sample posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External brands, agencies, restaurant chains, and food PR teams use this skill to identify and evaluate food creators for outreach, partnerships, and social media campaigns. It helps segment creators by platform, niche, engagement quality, and cross-platform presence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and scraped public social-media data are sent to Apify/apidojo actors.

Mitigation: Use a scoped Apify token where possible and avoid entering private campaign details as search terms.

Risk: The artifact recommends optional run_actor.js examples, but that helper is not included in this artifact.

Mitigation: Verify any local helper scripts before running the optional examples or use the documented Apify MCP and REST API paths instead.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-food-bloggers-and-creators)
- [API Dojo publisher profile](https://clawhub.ai/user/apidojo-io)
- [Apify Instagram actor API endpoint](https://api.apify.com/v2/acts/apidojo~instagram-scraper/runs?token=$APIFY_TOKEN)
- [Apify TikTok actor API endpoint](https://api.apify.com/v2/acts/apidojo~tiktok-scraper/runs?token=$APIFY_TOKEN)

## Skill Output:

**Output Type(s):** [Markdown, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown with tables, scoring formulas, and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs creator lists with platform counts, follower and engagement metrics, content themes, scores, sample posts, and cross-platform matches.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
