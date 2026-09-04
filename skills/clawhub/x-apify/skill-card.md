## Description:

Fetches public X/Twitter data through Apify actors, including tweet searches and user timelines, with normalized JSON or summary output and local caching.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbyczgw-cla](https://clawhub.ai/user/robbyczgw-cla)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and external users use this skill to fetch public X/Twitter search results and user timeline data through Apify for monitoring, research, or downstream analysis. It is useful when normalized output, repeat-query caching, or Apify proxy infrastructure is needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and returned public tweet data are sent to Apify and may be stored in a local cache.

Mitigation: Use appropriate public-data queries, keep APIFY_API_TOKEN secure, and use --no-cache or --clear-cache when cached results should not persist.

Risk: Apify actor usage can incur billing costs and the default actor has minimum-result and Free-plan limits.

Mitigation: Monitor Apify billing, use --max-results 50 or higher with the default actor, and confirm plan limits before bulk runs.

Risk: The skill exposes a URL mode, but the default actor does not support single-tweet or reply scraping.

Mitigation: Set APIFY_ACTOR_ID=apidojo~twitter-scraper-lite for specific tweet or reply workflows, or avoid relying on --url with the default actor.

## Reference(s):

- [ClawHub x-apify Skill Page](https://clawhub.ai/robbyczgw-cla/skills/x-apify)
- [Tweet Scraper V2 actor](https://apify.com/apidojo/tweet-scraper)
- [Apify Pricing](https://apify.com/pricing)
- [Get Apify API token](https://console.apify.com/account/integrations)
- [Twitter Advanced Search Syntax](https://github.com/igorbrigadir/twitter-advanced-search)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON or human-readable tweet result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires APIFY_API_TOKEN. Results may be cached locally; the default actor requires 50 or more tweets per query and does not support single-tweet or reply scraping.]

## Skill Version(s):

1.1.0 (source: frontmatter and changelog, released 2026-08-31)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
