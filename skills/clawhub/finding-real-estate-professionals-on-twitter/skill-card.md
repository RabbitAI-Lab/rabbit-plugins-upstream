## Description:

Finds real estate agents, brokers, property investors, and real estate professionals on Twitter/X using apidojo's Twitter User Scraper on Apify, returning usernames, bios, follower counts, verification status, locations, and websites for outreach prospecting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, marketing, PropTech, mortgage, and B2B service teams use this skill to discover and rank real estate professionals on Twitter/X for outreach. Agents can run the Apify Twitter User Scraper, collect profile fields, and classify prospects into outreach tiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill supports broad Twitter/X prospecting and social-graph collection.

Mitigation: Use small maxItems values, collect only data needed for a clear lawful purpose, and avoid follower, following, or retweeter scraping unless it is specifically justified.

Risk: Queries and actor inputs may reveal sensitive prospecting strategy or expose credentials if handled carelessly.

Mitigation: Keep APIFY_TOKEN in a secure secret store and avoid placing confidential targeting strategy in search terms or saved run inputs.

Risk: customMapFunction can alter upstream actor processing in ways reviewers may not expect.

Mitigation: Avoid customMapFunction unless the reviewer understands how the upstream actor executes it and has reviewed the function body.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-real-estate-professionals-on-twitter)
- [Apify Twitter User Scraper API endpoint](https://api.apify.com/v2/acts/apidojo~twitter-user-scraper/runs)
- [Publisher profile](https://clawhub.ai/user/apidojo-io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, files]

**Output Format:** [Markdown guidance with shell commands and JSON or CSV result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns profile data such as username, bio, follower count, verification status, location, and website, with optional score and tier labels.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
